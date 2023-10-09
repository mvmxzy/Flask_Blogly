from unittest import TestCase

from app import app
from models import db, User, Post, Tag, Post_Tag

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()

class UserModelTestCase(TestCase):
    """ Tests for User model """
    def setUp(self):
        """ Set up """
        User.query.delete()
        user_1 = User(first_name="Samantha", last_name="Wright", img_url="https://images.pexels.com/photos/9794338/pexels-photo-9794338.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=750&w=1260")
        db.session.add(user_1)
        db.session.commit()

        self.user_1 = user_1
    
    def tearDown(self):
        """ Tear Down """

        db.session.rollback()
    
    def test_get_full_name(self):
        full_name = self.user_1.get_full_name()
        self.assertEqual(full_name,"Wright, Samantha")

class PostModelTestCase(TestCase):
    """ Tests for Post model """
    
    def setUp(self):
        """ Set up """
        all_posts = Post.query.all()
        for post in all_posts:
            db.session.delete(post)
        db.session.commit()
        post_1 = Post(title="A New Post", content="This is a test post")
        db.session.add(post_1)
        db.session.commit()

        self.post_1 = post_1
    
    def tearDown(self):
        """ Tear Down """

        db.session.rollback()
    
    def test_display_date(self):
        date = self.post_1.display_date()
        self.assertEqual(len(date),16)