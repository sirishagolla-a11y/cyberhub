import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models import Investigation, Candidate, Source, Evidence

# In-memory SQLite database for isolated unit testing
TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture
def db_session():
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()

def test_database_tables_creation(db_session):
    tables = Base.metadata.tables.keys()
    assert "investigations" in tables
    assert "candidates" in tables
    assert "sources" in tables
    assert "evidence" in tables

def test_investigation_crud(db_session):
    inv = Investigation(
        name="Target Investigation",
        username="johndoe",
        context="OSINT search target",
        image_reference="/storage/images/target.jpg",
        status="pending"
    )
    db_session.add(inv)
    db_session.commit()
    db_session.refresh(inv)

    assert inv.id is not None
    assert inv.name == "Target Investigation"
    assert inv.username == "johndoe"
    assert inv.status == "pending"

    fetched = db_session.query(Investigation).filter_by(username="johndoe").first()
    assert fetched is not None
    assert fetched.id == inv.id
    assert fetched.name == "Target Investigation"

def test_relationships(db_session):
    inv = Investigation(name="Alpha Project", username="alice")
    db_session.add(inv)
    db_session.commit()

    cand = Candidate(
        investigation_id=inv.id,
        display_name="Alice Smith",
        username="alicesmith",
        organization="CyberSec Corp"
    )
    db_session.add(cand)

    src = Source(name="GitHub", source_type="osint_code", base_url="https://github.com")
    db_session.add(src)
    db_session.commit()

    ev = Evidence(
        candidate_id=cand.id,
        source_id=src.id,
        title="Public Repository Found",
        description="Public repository containing target alias",
        url="https://github.com/alicesmith/repo",
        verification_status="verified"
    )
    db_session.add(ev)
    db_session.commit()

    fetched_cand = db_session.query(Candidate).filter_by(id=cand.id).first()
    assert fetched_cand.investigation.name == "Alpha Project"
    assert len(fetched_cand.evidence) == 1
    assert fetched_cand.evidence[0].title == "Public Repository Found"
    assert fetched_cand.evidence[0].source.name == "GitHub"
