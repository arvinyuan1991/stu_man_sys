from datetime import datetime
from clastudent.models import ClassStudent
from courses.models import Courses
import time
from students.models import Student
from teachers.models import Teacher


# 定时根据课程更新教师和学生的课时及课时费
def databasehandler():
    """定时根据课程更新教师和学生的课时及课时费"""
    print('%s: databasehandler' % time.ctime())

    now = datetime.now()
    now_time = now.strftime('%Y-%m-%d %H:%M:%S')
    courses = Courses.objects.all()
    for course in courses:
        print(type(course.start_time))
        start_time = course.start_time.strftime('%Y-%m-%d %H:%M:%S')
        print(start_time)
        if start_time < now_time and course.is_delete == False:
            class_id = course.classes_id
            teacher_id = course.teacher_id
            student_money = course.student_money
            total_time = course.total_time
            teacher_money = course.teacher_money

            # 处理教师课时费
            teacher = Teacher.objects.get(id=teacher_id)
            teacher.total_money += teacher_money
            teacher.total_hour += total_time
            teacher.save()

            # 处理学生课时费及课时
            clastudents = ClassStudent.objects.filter(classes_id=class_id)
            for clastudent in clastudents:
                student = Student.objects.get(id=clastudent.student_id)
                student.use_hour += total_time
                student.remain_hour -= total_time
                student.remain_money -= student_money

                student.save()

            course.is_delete = True
            course.save()
