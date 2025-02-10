# exceptions - errors in runtime

# types: NameError, ValueError, TypeError, OSError

# purpose:
# - clear description
# - report, logging, monitoring
# - continue running program

# BaseException
#  ├── BaseExceptionGroup
#  ├── GeneratorExit
#  ├── KeyboardInterrupt
#  ├── SystemExit
#  └── Exception
#       ├── ArithmeticError
#       │    ├── FloatingPointError
#       │    ├── OverflowError
#       │    └── ZeroDivisionError
#       ├── AssertionError
#       ├── AttributeError
#       ├── BufferError
#       ├── EOFError
#       ├── ExceptionGroup [BaseExceptionGroup]
#       ├── ImportError
#       │    └── ModuleNotFoundError
#       ├── LookupError
#       │    ├── IndexError
#       │    └── KeyError
#       ├── MemoryError
#       ├── NameError
#       │    └── UnboundLocalError
#       ├── OSError
#       │    ├── BlockingIOError
#       │    ├── ChildProcessError
#       │    ├── ConnectionError
#       │    │    ├── BrokenPipeError
#       │    │    ├── ConnectionAbortedError
#       │    │    ├── ConnectionRefusedError
#       │    │    └── ConnectionResetError
#       │    ├── FileExistsError
#       │    ├── FileNotFoundError
#       │    ├── InterruptedError
#       │    ├── IsADirectoryError
#       │    ├── NotADirectoryError
#       │    ├── PermissionError
#       │    ├── ProcessLookupError
#       │    └── TimeoutError
#       ├── ReferenceError
#       ├── RuntimeError
#       │    ├── NotImplementedError
#       │    ├── PythonFinalizationError
#       │    └── RecursionError
#       ├── StopAsyncIteration
#       ├── StopIteration
#       ├── SyntaxError
#       │    └── IndentationError
#       │         └── TabError
#       ├── SystemError
#       ├── TypeError
#       ├── ValueError
#       │    └── UnicodeError
#       │         ├── UnicodeDecodeError
#       │         ├── UnicodeEncodeError
#       │         └── UnicodeTranslateError
#       └── Warning
#            ├── BytesWarning
#            ├── DeprecationWarning
#            ├── EncodingWarning
#            ├── FutureWarning
#            ├── ImportWarning
#            ├── PendingDeprecationWarning
#            ├── ResourceWarning
#            ├── RuntimeWarning
#            ├── SyntaxWarning
#            ├── UnicodeWarning
#            └── UserWarning




def func():
    a = 1 / 0



















class B(Exception):
    pass


class C(B):
    pass

class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")




















# assigning exc obj to a name

try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception type
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)


# raise explicitly
def validate_input(value):
    if value < 0:
        raise ValueError("Invalid value. Must be non-negative.")










# reraise without handling

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise  # shorter form (without exc obj or class)


# tracebacks and exc "chaining"

try:
    open("database.sqlite")
except OSError:
    raise RuntimeError("unable to handle error")


# indicate a reason / suppress it

def func():
    raise ConnectionError

try:
    func()
except ConnectionError as exc:
    raise RuntimeError('Failed to open database') from exc




# finally nuances

try:
    raise ValueError('value error!')
finally:
    print("finally")


# two returns (one in finally)
def bool_return():
    try:
        return True
    finally:
        return False  # won't reraise the exc

bool_return()




# Умова задачі:
#
# На вхід програма отримує:
#  1. Розміри поля у форматі NxM (наприклад, 5x6, де 5 — кількість рядків, а 6 — кількість стовпців).
#  2. Кількість мін (4).
#  3. Координати мін у форматі рядок:стовпець (наприклад: 1:1, 2:2, 3:2, 4:4).
#
# Завдання:
# На виході потрібно згенерувати поле заданих розмірів, де:
#  • У клітинці з міною — символ міни (наприклад, *).
#  • У клітинці без міни — кількість мін у сусідніх клітинках.
#
# Сусідніми вважаються клітинки, які межують по горизонталі, вертикалі чи діагоналі.
#
# Приклад:
# Вхідні дані:
#
# Розмір поля: 5x6
# Кількість мін: 4
# Координати мін: 1:1, 2:2, 3:3, 4:4
#
# Вихід:
#
# * 2 0 0 0 0
# 2 * 2 1 1 0
# 1 2 * 1 2 0
# 0 1 2 * 1 0
# 0 0 1 1 1 0


# beware: borders

def draw_board(size: str, n: int, coords: str):
    # parsing param
    rows, cols = map(int, size.split("x"))
    print(rows, cols)
    # coords to tuples
    coords = map(lambda s: (int(s[0]) - 1, int(s[2]) - 1), coords.split(", "))

    # draw empty board
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    # place mines
    for x, y in coords:
        board[x][y] = "*"
    print(board)

    # calc count in neighbours (skip if *, count 8 cells around (exclude self))

    def get_neighbours(i, j, board):
        ds = (-1, 0, 1)
        for di in ds:
            for dj in ds:
                ni = i + di
                nj = j + dj

                if di == 0 and dj == 0:
                    continue

                if 0 <= ni < rows and 0 <= nj < cols:
                    yield board[ni][nj]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "*":
                continue

            for val in get_neighbours(i, j, board):
                if val == "*":
                    board[i][j] += 1

    # print board

    for row in board:
        print([f"{v:>2}" for v in row])


draw_board("5x6", 4, "1:1, 2:2, 3:3, 4:4")
