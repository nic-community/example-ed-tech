from django.db.models import QuerySet

from .models import *


class HomeworkTaskRepository:

    @staticmethod
    def get_all():
        return HomeworkTaskModel.objects.all()
    
    @staticmethod
    def get_by_id(id):
        return HomeworkTaskModel.objects.get(id=id)
    
    @staticmethod
    def create(**kwargs):
        return HomeworkTaskModel.objects.create(**kwargs)
    
    @staticmethod
    def update(id, teacher, course, lesson, title, content):
        task = HomeworkTaskModel.objects.get(id=id)
        task.teacher = teacher
        task.course = course
        task.lesson = lesson
        task.title = title
        task.content = content
        
        task.save()
        return task
    
    @staticmethod
    def delete(id):
        task = HomeworkTaskModel.objects.get(id=id)
        task.delete()

    @staticmethod
    def filter(**kwargs):
        tasks = HomeworkTaskModel.objects.filter(**kwargs)
        return tasks
    

class HomeworkAnswerRepository:

    @staticmethod
    def get_all():
        return HomeworkAnswerModel.objects.all()
    
    @staticmethod
    def get_by_id(id):
        return HomeworkAnswerModel.objects.get(id=id)
    
    @staticmethod
    def create(**kwargs):
        return HomeworkAnswerModel.objects.create(**kwargs)
    
    @staticmethod
    def update(id, student, task, content, files):
        answer = HomeworkAnswerModel.objects.get(id=id)
        answer.student = student
        answer.task = task
        answer.files = files
        answer.content = content
        
        answer.save()
        return answer
    
    @staticmethod
    def delete(id):
        answer = HomeworkAnswerModel.objects.get(id=id)
        answer.delete()

    @staticmethod
    def filter(**kwargs):
        answer = HomeworkAnswerModel.objects.filter(**kwargs)
        return answer
    

class HomeworkGradeRepository:

    @staticmethod
    def get_all():
        return GradesForHomework.objects.all()
    
    @staticmethod
    def get_by_id(id):
        return GradesForHomework.objects.get(id=id)
    
    @staticmethod
    def create(**kwargs):
        return GradesForHomework.objects.create(**kwargs)
    
    @staticmethod
    def update(id, homework, comments, grade):
        grade_obj = GradesForHomework.objects.get(id=id)
        grade_obj.homework = homework
        grade_obj.comments = comments
        grade_obj.grade = grade
        
        grade_obj.save()
        return grade_obj
    
    @staticmethod
    def delete(id):
        grade = GradesForHomework.objects.get(id=id)
        grade.delete()

    @staticmethod
    def filter(**kwargs):
        grade = GradesForHomework.objects.filter(**kwargs)
        return grade