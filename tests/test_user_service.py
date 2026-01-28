from app.user_service import create_user, get_users, get_user, update_user, delete_user
from app.schemas import UserCreate, UserUpdate

def test_list_users(db_session):
    # Create sample users
    user1 = create_user(db_session, UserCreate(name="Pelle", email="pelle@test.com", age=28))
    user2 = create_user(db_session, UserCreate(name="Kalle", email="kalle@test.com", age=32))

    users = get_users(db_session)
    assert len(users) == 2
    assert any(user.email == "pelle@test.com" for user in users)
    assert any(user.email == "kalle@test.com" for user in users)

def test_create_user(db_session):
    # Create user data
    user_data = UserCreate(name="Selim", email="selim@test.com", age=25)
    
    # Create user
    new_user = create_user(db_session, user_data)
    
    # Verify user creation
    assert new_user.name == "Selim"
    assert new_user.id is not None
    
def test_get_user_by_id(db_session):
    # Create a user first
    user_in = UserCreate(name="Anna", email="anna@test.com", age=30)
    created = create_user(db_session, user_in)
    
    # Try to fetch user by ID
    fetched = get_user(db_session, created.id)
    assert fetched.email == "anna@test.com"

def test_update_user(db_session):
    # Create user
    created = create_user(db_session, UserCreate(name="Old Name", email="old@test.com", age=20))
    
    # Update user
    update_data = UserUpdate(name="New Name")
    updated = update_user(db_session, created.id, update_data)
    
    assert updated.name == "New Name"
    assert updated.email == "old@test.com" # Should remain unchanged

def test_delete_user(db_session):
    # Create user
    created = create_user(db_session, UserCreate(name="ToDelete", email="to_delete@test.com", age=40))

    # Delete user
    deleted = delete_user(db_session, created.id)
    # Try to fetch again
    should_be_none = get_user(db_session, created.id)

    assert deleted is not None
    assert should_be_none is None

