from app.models import Feedback,User
from app import db

def setUp(self):
        self.user_joy = User(username = 'joy',password = 'joy', email = 'joy@ms.com')
        self.new_review = Review(id=12345,image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",user = self.user_joy )


def tearDown(self):
        Feedback.query.delete()
        User.query.delete()

def test_check_instance_variables(self):
        self.assertEquals(self.new_feedback.id,12345)
        self.assertEquals(self.new_feedback.image_path,"https://image.tmdb.org/t/p/w500/jdjdjdjn")
        self.assertEquals(self.new_feedback.user,self.user_joy)


def test_save_feedback(self):
        self.new_feedback.save_feedback()
        self.assertTrue(len(Review.query.all())>0)        


def test_get_feedback_by_id(self):
    
        self.new_feedback.save_feedback()
        got_feedback = Feedback.get_feedback(12345)
        self.assertTrue(len(got_feedback) == 1)