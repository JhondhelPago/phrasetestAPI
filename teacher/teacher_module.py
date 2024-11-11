from user.models import CustomUser, studentuser
from student.models import essay_submitted, rubrics
from . models import section, essay_assignment



class student:

    def __init__(self, Student_Instance : CustomUser):
        
        self.user_studentuser = Student_Instance
        self.essay_submitted = None
        self.rubrics = None

    # call the function to get the instance of essay_submitted and rubrics on the constructor


    




def TeacherCreateSection(teacher_id):


    TeacherObj = CustomUser.objects.get(id=int(teacher_id))

    section_instance = section(teacher_id=teacher_id)

    section_instance.save()

#function that return the a a dictionary of submitted studet, unsubmitted student, total number of student, 
#get the date of submission for each student, get their label  from the using their rubrics by passing the essay_submmited parameter to model orm
def get_submitted_students(section_code, assignment_instance : essay_assignment):

    #get all of student in this section code
    student_list_obj = studentuser.objects.filter(section=section_code)
    student_list_ids = [student.user_id for student in student_list_obj]


    studentuser_QuerySet = CustomUser.objects.filter(id__in=student_list_ids) 
    # submitted_student_names = [student.first_name for student in studentuser_QuerySet]

    # get all of the ids who submitted on the assignment
    submitted_student = essay_submitted.objects.filter(student_id__in=student_list_ids).filter(assignment_code=assignment_instance.assignment_code)
    submitted_student_ids_demo = [student.student_id for student in submitted_student]
    print(f"submitted_student_ids: {submitted_student_ids_demo}")

    submitted_ids = submitted_student_ids_demo
    unsubmitted_ids = list()

    print(f"pre loop submitted_ids : {submitted_ids}")

    for id in student_list_ids:

        if not id in submitted_student_ids_demo:

            unsubmitted_ids.append(id)


    print(f"post lopp submitted_ids : {submitted_ids}")
    print(f"post loop unsubmitted_ids : {unsubmitted_ids}")

    submitted_student_count = len(submitted_ids)
    unsubmitted_student_count = len(unsubmitted_ids)

            
    #student object from the CustomUser Model
    unsubmitted_student = CustomUser.objects.filter(id__in=unsubmitted_ids)
    submitted_student = CustomUser.objects.filter(id__in=submitted_ids)


    #using the student_id get the essay_submited_instance

    essay_submitted_students = essay_submitted.objects.filter(student_id__in=submitted_ids).filter(assignment_code=assignment_instance.assignment_code)



    # using the submitted_student get the date date properties
    submitted_date_list = [essay_submitted_instance.get_date_submitted()  for essay_submitted_instance in essay_submitted_students]

    #get the names of submitted student
    submmited_names = [student.last_name + ', '  + student.first_name for student in submitted_student]


    #get the label os the student using the essay_submitted.id
    essay_submitted_FK_from_submitted_student = [essay_submitted_instance.id for essay_submitted_instance in essay_submitted_students]

    rubrics_instances = rubrics.objects.filter(essay_submitted__in=essay_submitted_FK_from_submitted_student)
    rubrics_label_list = [rubrics_instance.label for rubrics_instance in rubrics_instances]



    #get the names of unsubmitted student


    return {
        "submitted" : submitted_student_count,
        "submitted_names" : submmited_names,
        "refernce_essay_submitted_key" : essay_submitted_FK_from_submitted_student,
        "dates" : submitted_date_list,
        "labels" : rubrics_label_list,
        "unsubmitted" : unsubmitted_student_count,
    }
