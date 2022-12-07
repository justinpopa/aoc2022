from aocd.models import Puzzle
import re
from anytree import Node, RenderTree

puzzle = Puzzle(year=2022, day=7)

input = puzzle.input_data

FILESYSTEM_SIZE = 70000000
UPDATE_SIZE = 30000000

def get_size(node):
    return sum(get_size(n) for n in node.children) if node.type == 'dir' else node.size

root = Node('', parent=None, type='dir')
cur_node = root

for line in input.splitlines():
    if bool(re.match('^\$', line)):
        if line[2:4] == 'cd' and line[5:] != '/':
            if line[5:] != '..':
                node = Node(line[5:], parent=cur_node, type='dir')
                cur_node = node
            else:
                cur_node = cur_node.parent
    else:
        if bool(re.match('^\d+', line)):
            Node(line[line.find(' ') + 1:], parent=cur_node, size=int(line[:line.find(' ')]), type='file')

answer1 = []
answer2 = []

for pre, fill, node in RenderTree(root):
    if node.type == 'dir' and get_size(node) <= 100000:
        answer1.append(get_size(node))

print(sum(answer1))

cleanup_needed = get_size(root) - (FILESYSTEM_SIZE - UPDATE_SIZE)

nodes = []
for pre, fill, node in RenderTree(root):
    if node.type == 'dir' and get_size(node) >= cleanup_needed:
        nodes.append(node)

node_nums = [get_size(n) for n in nodes]
node_nums.sort()
print(node_nums[0])