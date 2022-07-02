import unittest


class BidirectionalLinkedList(object):

    SPECIAL_KEYS = ["01", "12", "23", "34", "45", "56", "67", "78", "89", "90"]
    SPECIALS = {
        "01": "2",
        "12": "3",
        "23": "4",
        "34": "5",
        "45": "6",
        "56": "7",
        "67": "8",
        "78": "9",
        "89": "0",
        "90": "1",
    }

    def __init__(self, s):
        self.head = None
        self.poi = dict((special, set()) for special in self.SPECIAL_KEYS)
        prev = None
        for letter in s:
            node = Node(letter)
            if prev:
                prev.next_node = node
                node.prev_node = prev
                if self.nodes_are_interesting(prev, node):
                    self.add_interesting(prev, node)
            else:
                self.head = node
            prev = node

    def transform(self):
        while any(self.poi.get(s) for s in self.SPECIAL_KEYS):
            for special in self.SPECIAL_KEYS:
                for node in self.poi.get(special):
                    if self.nodes_are_interesting(node, node.next_node):
                        node.data = self.SPECIALS.get(special)
                        node.next_node = node.next_node.next_node
                        if node.prev_node and self.nodes_are_interesting(
                            node.prev_node, node
                        ):
                            self.add_interesting(node.prev_node, node)
                        if node.next_node:
                            node.next_node.prev_node = node
                            if self.nodes_are_interesting(node, node.next_node):
                                self.add_interesting(node, node.next_node)
                self.poi[special].clear()

    def add_interesting(self, node1, node2):
        self.poi[node1.data + node2.data].add(node1)

    def nodes_are_interesting(self, node1, node2):
        return (
            self.nodes_in_order(node1, node2)
            and node1.data + node2.data in self.SPECIALS
        )

    def nodes_in_order(self, node1, node2):
        return node1.next_node == node2 and node2.prev_node == node1

    def to_string(self):
        new_s = ""
        node = self.head
        while node:
            new_s += node.data
            node = node.next_node
        return new_s


class Node(object):
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node


def silly_submissions(s):
    bdll = BidirectionalLinkedList(s)
    bdll.transform()
    return bdll.to_string()


class TestSillySubmissions(unittest.TestCase):
    def test_sample0(self):
        self.assertEqual(silly_submissions("1"), "1")

    def test_sample1(self):
        self.assertEqual(silly_submissions("012"), "22")

    def test_sample2(self):
        self.assertEqual(silly_submissions("0145"), "26")

    def test_sample3(self):
        self.assertEqual(silly_submissions("00000"), "00000")

    def test_sample4(self):
        self.assertEqual(silly_submissions("98765432101"), "1")


if __name__ == "__main__":
    unittest.main()
