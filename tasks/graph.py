from collections import deque
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        result = []
        stack = deque()
        stack.append(self._root)
        while len(stack):
            v = stack.pop()
            if v not in result:
                result.append(v)
                for i in v.outbound[::-1]:
                    stack.append(i)
        return result

    def bfs(self) -> list[Node]:
        result = []
        queue = deque()
        queue.append(self._root)
        while len(queue):
            v = queue.popleft()
            if v not in result:
                result.append(v)
                for t in v.outbound:
                    queue.append(t)

        return result
