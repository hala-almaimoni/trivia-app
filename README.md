# Trivia API Project

## Introduction
This project is python/react version of trivia application, you can display all questions, dispaly questions based on category, delete a question, create a question and take a quick quize.

## Getting Started

### Pre-requisites and Local Development
Developers using this project should already have Python3, pip and node installed on their local machines.

## Backend
From the backend folder run the following command to install All required packages:
```bash
pip install -r requirements.txt
```
To run the application run the following commands:
```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```
These commands put the application in development and directs our application to use the `__init__.py` file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made.
The application is run on http://127.0.0.1:5000/ by default.

## Frontend
From the frontend folder, run the following commands to start the client:
```bash
npm install // only once to install dependencies
npm start
```
By default, the frontend will run on localhost:3000.

## Tests
In order to run tests navigate to the backend folder and run the following commands:
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
The first time you run the tests, omit the dropdb command.

## API Reference
GET /categories
* General:
    * Returns a list of category objects and success value.
* Sample: curl http://127.0.0.1:5000/categories
```
  {
    "categories": [
    {
        "id": 1,
        "type": "Science"
        },
        {
        "id": 2,
        "type": "Art"
        },
        {
        "id": 3,
        "type": "Geography"
        },
        {
        "id": 4,
        "type": "History"
        },
        {
        "id": 5,
        "type": "Entertainment"
        },
        {
        "id": 6,
        "type": "Sports"
        }
    ],
    "success": true
}
```
GET /qustions
* General:
    * Returns a list of catgory objects, question objects, success value and total number of questions.
    * Results are paginated in groups of 10. Include a request argument to choose page number, starting from 1.
* Sample: curl http://127.0.0.1:5000/qustions
```
{
    "categories": [
    {
        "id": 1,
        "type": "Science"
        },
        {
        "id": 2,
        "type": "Art"
        },
        {
        "id": 3,
        "type": "Geography"
        },
        {
        "id": 4,
        "type": "History"
        },
        {
        "id": 5,
        "type": "Entertainment"
        },
        {
        "id": 6,
        "type": "Sports"
        }
    ],
    "questions": [
        {
        "answer": "Maya Angelou",
        "category": 4,
        "difficulty": 2,
        "id": 5,
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
        "answer": "Muhammad Ali",
        "category": 4,
        "difficulty": 1,
        "id": 9,
        "question": "What boxer's original name is Cassius Clay?"
        },
        {
        "answer": "Apollo 13",
        "category": 5,
        "difficulty": 4,
        "id": 2,
        "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
        },
        {
        "answer": "Tom Cruise",
        "category": 5,
        "difficulty": 4,
        "id": 4,
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
        },
        {
        "answer": "Edward Scissorhands",
        "category": 5,
        "difficulty": 3,
        "id": 6,
        "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        },
        {
        "answer": "Brazil",
        "category": 6,
        "difficulty": 3,
        "id": 10,
        "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
        "answer": "Uruguay",
        "category": 6,
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?"
        },
        {
        "answer": "George Washington Carver",
        "category": 4,
        "difficulty": 2,
        "id": 12,
        "question": "Who invented Peanut Butter?"
        },
        {
        "answer": "Lake Victoria",
        "category": 3,
        "difficulty": 2,
        "id": 13,
        "question": "What is the largest lake in Africa?"
        },
        {
        "answer": "The Palace of Versailles",
        "category": 3,
        "difficulty": 3,
        "id": 14,
        "question": "In which royal palace would you find the Hall of Mirrors?"
        }
    ],
    "success": true,
    "total_questions": 19

}
```
GET /categories/{category_id}/questions
* General:
    * Returns a list of question objects based on category and success value.
* Sample: curl http://127.0.0.1:5000/categories/1/questions
```
{
    "questions": [
        {
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 20,
        "question": "What is the heaviest organ in the human body?"
        },
        {
        "answer": "Alexander Fleming",
        "category": 1,
        "difficulty": 3,
        "id": 21,
        "question": "Who discovered penicillin?"
        },
        {
        "answer": "Blood",
        "category": 1,
        "difficulty": 4,
        "id": 22,
        "question": "Hematology is a branch of medicine involving the study of what?"
        }
    ],
    "success": true

}
```
POST /questions
 * General:
    * Creates a new book using the submitted question, answer, category and difficulty. Returns the success value.
 * curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"Which country will host Cricket World Cup 2019?", "answer":"England", "category":6, "difficulty":4}'
 ```
 {
 "success": true,
 }
 ```
  DELETE /questions/{question_id} 
 * General:
    * Deletes the question of the given ID if it exists. Returns the success value.
* curl -X DELETE http://127.0.0.1:5000/questions/1
```
 {
 "success": true,
 }
 ```
  POST /questions/search 
* General:
    * Returns a list of question objects for whom the search term is a substring of the question, success value and total number of returned questions.
* curl http://127.0.0.1:5000/books/15 -X POST -H "Content-Type: application/json" -d '{"searchTerm":"soccer"}' 
 ```
{ 
    "questions":[
        {
        "answer": "Brazil",
        "category": 6,
        "difficulty": 3,
        "id": 10,
        "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
        "answer": "Uruguay",
        "category": 6,
        "difficulty": 4,
        "id": 11,
        "question": "Which country won the first ever soccer World Cup in 1930?"
        }
    ], 
    "success": true,
    "total_questions": 2
}
```
 POST /quizzes 
* General:
    * Returns a one question object within the given category question and success value.
* curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {'id': 1, 'type': 'Science'}}' 
 ```
{ 
    "question":{
        "answer": "The Liver",
        "category": 1,
        "difficulty": 4,
        "id": 10,
        "question": "What is the heaviest organ in the human body?"
        },
    "success": true
}
```
## Authors
* Hala Almaimoni

## Acknowledgements
Many thanks to Udacity team, my session lead Ms. Elham Jaffar and my colleagues for all the assistance and support