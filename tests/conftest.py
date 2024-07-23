import sys
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, drop_database, create_database
from app.database import Base
from app.main import app
from fastapi.testclient import TestClient

# プロジェクトのルートディレクトリをPythonのパスに追加
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")

# テスト用データベースURL
TEST_SQLALCHEMY_DATABASE_URL = "sqlite:///./test_temp.db"

@pytest.fixture(scope="session")
def db():
    # データベースの設定
    engine = create_engine(TEST_SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

    # テストデータベースが既に存在する場合は削除
    if database_exists(TEST_SQLALCHEMY_DATABASE_URL):
        drop_database(TEST_SQLALCHEMY_DATABASE_URL)
    
    # テストデータベースの作成
    create_database(TEST_SQLALCHEMY_DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # セッションを返す
    db = TestingSessionLocal()
    yield db
    
    # テストデータベースをクリーンアップ
    db.close()
    Base.metadata.drop_all(bind=engine)
    drop_database(TEST_SQLALCHEMY_DATABASE_URL)

@pytest.fixture(scope="function")
def test_db(db):
    # 全テーブルのデータを削除
    meta = Base.metadata
    for table in reversed(meta.sorted_tables):
        db.execute(table.delete())
    db.commit()
    return db

@pytest.fixture(scope="function")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            db.close()
    
    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as c:
        yield c