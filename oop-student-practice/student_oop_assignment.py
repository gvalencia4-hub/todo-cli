import re


class Student:
    """
    Represents a student with a name, email, and a list of integer grades.
    """

    def __init__(self, name: str, email: str, grades: list[int]):
        self.name = name
        self.email = email
        self.grades = grades

    def add_grade(self, grade: int) -> None:
        """Adds a grade (int) to the grades list."""
        self.grades.append(grade)

    def average_grade(self) -> float:
        """Returns the average of all grades. Returns 0.0 if there are no grades."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def display_info(self) -> None:
        """Prints the student's name, email, and grades."""
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.average_grade():.2f}")
        print("-" * 40)

    def grades_tuple(self) -> tuple:
        """Returns the grades list as an immutable tuple."""
        return tuple(self.grades)



def get_student_by_email(student_dict: dict, email: str):
    """
    Safely retrieves a Student object from the dictionary using .get().
    Returns None if not found.
    """
    return student_dict.get(email)


def is_valid_email(email: str) -> bool:
    """
    Bonus: Validates email format like name@domain.com using regex.
    This is a simple pattern for learning purposes.
    """
    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    return re.match(pattern, email) is not None


def main():
    
    student1 = Student("Alice Johnson", "alice@example.com", [88, 92, 79])
    student2 = Student("Brian Smith", "brian.smith@example.com", [95, 87, 90])
    student3 = Student("Carla Reyes", "carla.reyes@example.com", [100, 84, 91])

    students = [student1, student2, student3]

   
    student1.add_grade(85)
    student1.add_grade(93)

    student2.add_grade(76)
    student2.add_grade(99)

    student3.add_grade(89)
    student3.add_grade(97)

    
    print("\n=== Student Info (After Adding Grades) ===")
    for s in students:
        s.display_info()

    
    student_dict = {s.email: s for s in students}

   
    print("\n=== Lookup Student by Email ===")
    lookup_email = "brian.smith@example.com"
    found = get_student_by_email(student_dict, lookup_email)
    if found:
        print(f"Found student for {lookup_email}: {found.name}")
    else:
        print(f"No student found for {lookup_email}")

    
    unique_grades = set()
    for s in students:
        unique_grades.update(s.grades)

    print("\n=== Unique Grades Across All Students ===")
    print(unique_grades)

    
    print("\n=== Tuple Immutability Demo ===")
    t = student1.grades_tuple()
    print("Grades tuple:", t)

    try:
        
        t[0] = 999
    except TypeError:
        print("Tuples are immutable: you cannot change values inside a tuple.")

    
    print("\n=== List Operations ===")
    for s in students:
        if s.grades:
            removed = s.grades.pop()  
            print(f"{s.name}: popped last grade ({removed}). Remaining grades: {s.grades}")

            
            if s.grades:
                print(f"{s.name}: first grade = {s.grades[0]}, last grade = {s.grades[-1]}")
            else:
                print(f"{s.name}: no grades left after popping!")

            print(f"{s.name}: number of grades = {len(s.grades)}")
            print("-" * 40)
        else:
            print(f"{s.name}: No grades to pop.")
            print("-" * 40)

  
    print("\n=== Email Validation (Bonus) ===")
    for s in students:
        if is_valid_email(s.email):
            print(f"✅ Valid email: {s.email}")
        else:
            print(f"❌ Invalid email: {s.email}")

  
    print("\n=== Count Grades > 90 (Bonus) ===")
    count_above_90 = 0
    for s in students:
        count_above_90 += sum(1 for g in s.grades if g > 90)

    print("Total grades above 90 across all students:", count_above_90)


if __name__ == "__main__":
    main()

