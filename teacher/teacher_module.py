from user.models import CustomUser
from . models import section



def TeacherCreateSection(teacher_id):


    TeacherObj = CustomUser.objects.get(id=int(teacher_id))

    section_instance = section(teacher_id=teacher_id)

    section_instance.save()