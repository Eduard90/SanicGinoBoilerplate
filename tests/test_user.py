from tests import BaseTestCase
from models import User


class UserTestCase(BaseTestCase):
    async def test_user_created(self):
        user = await User.create(username='user1', name='user1 Name', password='123', email='user@user.ru')
        self.assertEqual(user.id, 1)

