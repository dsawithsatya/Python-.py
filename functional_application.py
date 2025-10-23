# We are going to implement a worker application using the functional programming language 
#first we have to check the login details
"""
def database():
    return {
        "satya":"pass123",
        "siva":"pass143",
        "kaja":"pass420" }
def login_credentials(user_name,password,data):
    if user_name not in data:
        print("you entered username or password incorrectly ")
    elif password not in data :
        print("you entered username or password incorrectly ") 
        
    else:
        print("Login successfully...")
if(__name__=="__main__"):
    login_credentials(user_name=input("Enter user_name"),password=input("Enter a password "),data=database())
"""

def get_workers():
    return [
        {"id": 1, "name": "Satya", "skill": "Python", "available": True},
        {"id": 2, "name": "Siva", "skill": "Java", "available": True},
        {"id": 3, "name": "Khaja", "skill": "MERN Stack", "available": False}    ]

def get_available_workers(workers):
    return list(filter(lambda w: w["available"], workers))
def check_id(workers,worker_id):
    if get_workers !=worker_id:
        return "Enter a valid id"

def book_worker(workers, worker_id):
    return list(map(lambda w: {**w, "available": False} if w["id"] == worker_id else w, workers))

def show_workers(workers):
    print("\nAvailable Workers:")
    for w in get_available_workers(workers):
        print(f"ID: {w['id']} | Name: {w['name']} | Skill: {w['skill']}")
    print()


if __name__ == "__main__":
    workers = get_workers()
    show_workers(workers)

    #worker_id = int(input("Enter the worker ID you want to book: "))
    workers = book_worker(workers, worker_id=int(input("Enter the worker ID you want to book : ")))
    

    print("\n Booking successful..")
    show_workers(workers)

