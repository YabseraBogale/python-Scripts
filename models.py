from django.db import models
#from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
import random
import string



# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    father_name = models.CharField(max_length=20, null=False)
    grandfather_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=100, unique=True, null=False)
    phone_number = models.CharField(max_length=20, blank = False, unique = True )
    password = models.CharField(max_length=50, null=False)
    # for the front end and use session and cookie
    paasword_cofirmation = models.CharField(max_length=50, null=False)
    registration_date = models.DateTimeField(auto_now_add=True)
   
    @property
    def get_name(self):
        return self.User.first_name+" "+self.User.father_name+" "+self.User.grandfather_name
    @property
    def get_id(self):
        return self.User.id
    def __str__(self):
        return self.User.first_name
    
class Topics(models.Model):
    topic_name = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.topic_name



class Course(models.Model):
    content_title = models.CharField(max_length=50, null=False)
    video = models.FileField(upload_to='media/course_files')
    description = RichTextField(blank=False, null=False)
    image = models.FileField(blank = False, null = False)
    thumb = models.FileField()
    course_materials = models.FileField(upload_to='media/course_files',null = True, blank=True)
    learnig_outcome = RichTextField(blank = True, null = True)
    pre_requirement = RichTextField(blank = True, null = True)
    instructor = models.CharField(max_length = 30, blank = False, null = False)
    topics = models.ForeignKey(Topics, on_delete=models.CASCADE)
    price = models.FloatField()
    #acting like promo code
    course_code = models.CharField(max_length=10, unique=True)

    def code_generate(self):
        code = ''
        for i in range(10):
            code += random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
        return code
        
    def save(self, *args, **kwargs):
        if not self.code:
            self.code = self.code_generate()
        super().save(*args, **kwargs)        
    


class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(null=True, blank=True, default=0)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.rating)
    

class Featured_course(models.Model):    
    title = models.CharField(max_length=500)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='featured_course')

    def __str__(self):
        return self.Course.title
    
class enrolled_coures(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL)    



class Wishlist(models.Model):
    User = models.ForeignKey( User, on_delete=models.CASCADE, related_name='wishlists')
    Course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='wishlist_course')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.User} for the  {self.Course}"



class Questions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.SET_NULL)
    question = models.TextField()

    

class Answers(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name="answer")
    answer = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.answer


class Certificate(models.Model):
    user = models.ForeignKey( User, on_delete=models.SET_NULL, related_name="certificates")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, related_name="certificates")
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.User}'s certificate for {self.Course}"

class faq(models.Model):    
    title = models.CharField(max_length=300, blank = False)
    content = RichTextField(blank=False)    


# don't forget about terms and serverce



