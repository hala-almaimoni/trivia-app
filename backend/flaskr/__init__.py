import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from flask_migrate import Migrate

from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  migrate = Migrate(app, db)
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
    return response
    
  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories')
  def get_categories():
    categories = Category.query.all()
    formatted_categories = [category.format() for category in categories]
    return jsonify({
      'success': True,
      'categories': formatted_categories
    })


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 
  '''
  @app.route('/questions')
  def get_questions():
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10
    questions = Question.query.all()
    formatted_questions = [question.format() for question in questions]
    categories = Category.query.all()
    formatted_categories = [category.format() for category in categories]
    return jsonify({
      'success': True,
      'questions': formatted_questions[start:end],
      'total_questions': len(formatted_questions),
      'categories': formatted_categories,
    })
  '''
  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.get(question_id)
    if question is None:
        abort(404)
        
    question.delete()
    return jsonify({
      'success': True
    })
  '''
  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.
  '''
  @app.route('/questions', methods=['POST'])
  def create_question():
    body = request.get_json()
    question = body.get('question')
    answer = body.get('answer')
    category = body.get('category')
    difficulty = int(body.get('difficulty'))
    new_question = Question(question=question, answer=answer, category=category, difficulty=difficulty)
    Question.insert(new_question)
    return jsonify({
      'success': True
    })
  '''
  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 
  '''
  @app.route('/questions/search', methods=['POST'])
  def search_question():
    body = request.get_json()
    search_term = body.get('searchTerm')
    questions = Question.query.filter(Question.question.ilike(f'%{search_term}%'))
    formatted_questions = [question.format() for question in questions]
    return jsonify({
      'success': True,
      'questions': formatted_questions,
      'total_questions': len(formatted_questions)
    })
  '''
  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  def get_category_questions(category_id):
    questions = Question.query.filter_by(category=category_id)
    formatted_questions = [question.format() for question in questions]

    return jsonify({
      'success': True,
      'questions': formatted_questions
    })

  '''
  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def play():
    body = request.get_json()
    previous_questions = body.get('previous_questions')
    quiz_category = body.get('quiz_category')
    index = len(previous_questions)
    print(quiz_category)
    if quiz_category["id"] == 0:
      questions = Question.query.all()
      formatted_questions = [question.format() for question in questions]
    else:
      questions = Question.query.filter_by(category=quiz_category["id"]).all()
      formatted_questions = [question.format() for question in questions]
    if len(previous_questions) == len(questions):
      next_question = None
    else:
      next_question = formatted_questions[index]
    return jsonify({
      'success': True,
      'question': next_question
    })
  '''
  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False, 
        "error": 404,
        "message": "Not found"
        }), 404


  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      "success": False, 
      "error": 422,
      "message": "unprocessable"
      }), 422

  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 400,
      "message": "bad request"
      }), 400

  @app.errorhandler(500)
  def bad_request(error):
    return jsonify({
      "success": False, 
      "error": 500,
      "message": "Internal Server Error"
      }), 400
  
  return app

    