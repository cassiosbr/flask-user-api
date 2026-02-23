from types import SimpleNamespace
from unittest.mock import Mock
from app.services.user_service import UserService

def test_create_user_success():
    mock_repo = Mock()
    mock_repo.get_user_by_email.return_value = None
    mock_repo.create_user.return_value = SimpleNamespace(id=1, name='Test User', email='test@example.com')

    user_service = UserService(user_repository=mock_repo)
    user = user_service.create_user('Test User', 'test@example.com')

    mock_repo.get_user_by_email.assert_called_once_with('test@example.com')
    mock_repo.create_user.assert_called_once_with('Test User', 'test@example.com')

    assert user.id == 1
    assert user.name == 'Test User'
    assert user.email == 'test@example.com'

def test_create_user_missing_fields():
    user_service = UserService(user_repository=Mock())
    
    try:
        user_service.create_user('', '')
    except ValueError as e:
        assert str(e) == 'Nome e email são obrigatórios'

def test_create_user_long_name():
    mock_repo = Mock()
    service = UserService(user_repository=mock_repo)

    long_name = "a" * 101

    try:
        service.create_user(long_name, "email@test.com")
    except ValueError as e:
        assert str(e) == "Nome deve ter 100 caracteres ou menos"

    mock_repo.create_user.assert_not_called()
    