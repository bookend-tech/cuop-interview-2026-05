"""
이 과제는 AI 사용이 불가합니다.

아래 TODO 영역의 SQL만 수정해서 테스트를 통과시키세요.
users 테이블에서 나이가 20세 이상인 사용자의 name만 조회해야 합니다.

실행 방법:
    python d_sql_select_question.py
"""

import sqlite3
from typing import List, Tuple


EXPECTED_NAMES = ["Alice", "Charlie"]


def get_sql() -> str:
    """TODO 영역의 SQL만 수정하세요."""
    # 여기서부터 코드를 수정하세요
    return """
        SELECT name
        FROM users
        WHERE age < 20
        ORDER BY id;
    """
    # 여기까지 코드를 수정하세요


def create_database() -> sqlite3.Connection:
    conn = sqlite3.connect(":memory:")
    conn.execute(
        """
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        );
        """
    )
    conn.executemany(
        "INSERT INTO users (id, name, age) VALUES (?, ?, ?);",
        [
            (1, "Alice", 24),
            (2, "Bob", 17),
            (3, "Charlie", 20),
            (4, "Diana", 14),
        ],
    )
    return conn


def run_query(conn: sqlite3.Connection, sql: str) -> List[str]:
    rows: List[Tuple[str]] = conn.execute(sql).fetchall()
    return [name for (name,) in rows]


def run_tests() -> None:
    conn = create_database()

    try:
        actual_names = run_query(conn, get_sql())
    except sqlite3.Error as exc:
        print("FAIL")
        print(f"SQL 실행 중 오류가 발생했습니다: {exc}")
        return
    finally:
        conn.close()

    if actual_names == EXPECTED_NAMES:
        print("PASS")
        print(f"결과: {actual_names}")
        return

    print("FAIL")
    print(f"기대 결과: {EXPECTED_NAMES}")
    print(f"실제 결과: {actual_names}")


if __name__ == "__main__":
    run_tests()
