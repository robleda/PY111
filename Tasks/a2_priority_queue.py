"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

pq = {i: [] for i in range(6)}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    pq[priority].insert(0, elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """
    for priority in pq.keys():
        if not pq[priority]:
            continue
        else:
            return pq[priority].pop()
    else:
        return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if ind <= (len(pq[priority]) - 1):
        q = pq[priority]
        return q[len(q) - ind - 1]
    else:
        return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    for priority in pq.keys():
        pq[priority].clear()
    return None
