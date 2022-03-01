import pytest

stack = []


def test_stack():
    # Добавляем два элемента в стек и затем извлекаем их
    # Почему два? Так надежнее, чем один, а три скорее всего избыточно
    stack.append('one')
    stack.append('two')
    assert stack.pop() == 'two'
    assert stack.pop() == 'one'


def test_emptiness():
    assert not stack
    stack.append('one')
    assert bool(stack)  # not not stack

    stack.pop()
    assert not stack


def test_pop_with_empty_stack():
    with pytest.raises(IndexError):
        stack.pop()
