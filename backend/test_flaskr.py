import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://hala@{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)
        questions = Question.query.all()
        formatted_questions = [question.format() for question in questions]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'], formatted_questions)


    def test_search_question(self):
        res = self.client().post('/questions/search', json={'searchTerm': 'The Taj Mahal is located in which Indian city?'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
    
    def test_delete_question(self):
        res = self.client().delete('/questions/12')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    def test_get_category_questions(self):
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)
        questions = Question.query.filter_by(category=1).all()
        formatted_questions = [question.format() for question in questions]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'], formatted_questions)
    

    def test_404_if_question_does_not_exist(self):
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')
    
    def test_create_new_question(self):
        res = self.client().post('/questions', json={'question': 'aaa', 'answer': 'bbb', 'category': 1, 'difficulty': 1})
        data = json.loads(res.data)
        pass
    
    def test_400_if_book_creation_fails(self):
        res = self.client().post('/books', json={'question': 'aaa', 'answer': 'bbb', 'category': 1, 'difficulty': 'high'})
        data = json.loads(res.data)
        pass

    def test_get_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)
        categories = Category.query.all()
        formatted_categories = [category.format() for category in categories]

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'], formatted_categories)

    def test_play(self):
        res = self.client().post('/quizzes', json={'previous_questions': [], 'quiz_category': {'id': 1, 'type': 'Science'}})
        data = json.loads(res.data)
        pass
    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()