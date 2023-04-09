from utils import Answer, Question, exercise

@exercise
def dictionaries():
  
  ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
  }
  
  # Question 1 
  Question(1, """
    How many students are in the dictionary?
  """)
  
  Answer(len(ages))
  
  # Question 2 
  Question(2, """
    Implement a function recieves the "ages" dictionary as parameters 
    and returns the average age of the students. Use the 'items' method.
  """)
  
  def average_age(dict):
    values = []
    for key, value in dict.items():
      values.append(value)
  
    return (sum(values) / len(values))
  
  
  Answer(average_age(ages))
  
  #3 
  Question(3, """
    Implement a function that recieves the 'age' dictionary as parameters
    and returns the name of the oldest student.
  """)
  
  
  def oldest_student(dict):
    oldest_age = 0
    for student, age in dict.items():
      if age > oldest_age:
        oldest_age = age
        oldest_student = student
  
    return oldest_student
  
  
  Answer(f"The oldest student is: {oldest_student(ages)}")
  
  # Question 4 
  Question(4, """
    Implement a function that recieves the 'ages' dictionary 
    and a number 'n' and returns a new dict where each student 
    is (n) year older. For Instance, new_ages(age, 10) returns a 
    copy of 'ages' where each student is 10 years older.
  """)
  
  
  def new_ages(dict, n):
    new_dict = {}
    for student, age in dict.items():
      new_dict.update({student: age + n})
    return new_dict
  
  
  Answer(f"{new_ages(ages, 10)}")
