import pytest
import asyncio
import time
import threading
from ..exercises.exercise_97 import add_matrices
from ..exercises.exercise_98 import process_data
from ..exercises.exercise_99 import BankAccount
from ..exercises.exercise_100 import time_it

NO_OF_THREADS = 5


def test_e97():
    assert add_matrices(
        matrix1=[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        matrix2=[[9, 8, 7], [6, 5, 4], [3, 2, 1]],
    ) == [
        [10, 10, 10],
        [10, 10, 10],
        [10, 10, 10],
    ]
    assert add_matrices(
        matrix1=[[1, 2, 3], [3, 2, 1], [1, 2, 3]],
        matrix2=[[-1, -2, -3], [-3, -2, -1], [-1, -2, -3]],
    ) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]


@pytest.mark.asyncio
async def test_e98():
    sources = ["source1", "source2", "source3"]
    results = await process_data(sources)
    assert len(results) == len(sources)
    assert set(results) == {f"Data from {source}" for source in sources}


def test_e99():
    account = BankAccount(name="Test Account", balance=0)

    def deposit_task():
        for _ in range(10):
            account.deposit(10)

    deposit_threads = [
        threading.Thread(target=deposit_task) for _ in range(NO_OF_THREADS)
    ]
    for thread in deposit_threads:
        thread.start()
    for thread in deposit_threads:
        thread.join()

    assert account.balance == 500

    account.deposit(250)  # Deposit from main thread

    def withdraw_task():
        for _ in range(10):
            account.withdraw(5)

    withdraw_threads = [
        threading.Thread(target=withdraw_task) for _ in range(NO_OF_THREADS)
    ]
    for thread in withdraw_threads:
        thread.start()
    for thread in withdraw_threads:
        thread.join()

    assert account.balance == 500

    with pytest.raises(ValueError):
        account.withdraw(1000)


def test_e100(capsys):
    @time_it
    def sync_func() -> None:
        time.sleep(0.5)

    sync_func()
    captured = capsys.readouterr()
    assert f"Time taken for {sync_func.__name__}:" in captured.out
    assert "0.5" in captured.out

    @time_it
    async def async_func() -> None:
        await asyncio.sleep(0.2)

    asyncio.run(async_func())
    captured = capsys.readouterr()
    assert f"Time taken for {async_func.__name__}:" in captured.out
    assert "0.2" in captured.out
