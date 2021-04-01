from django.db import models
from djongo import models as djmodels
# Create your models here.

# class GhazalsQueryset(djmodels.QuerySet):
#     def get_cleaned_content(self):
#         print(self)
# gazalManager = GhazalsQueryset.get_cleaned_content()



class Ghazals(djmodels.Model):
    _id = djmodels.ObjectIdField()
    ghazal_name = djmodels.TextField(max_length = 200,blank=True)
    author_name = djmodels.CharField(max_length = 200,blank=True)
    ghazal_content = djmodels.TextField(max_length = 2000,blank= True)
    author_alphabet = djmodels.CharField(max_length=1,blank=True)
    word_count = djmodels.IntegerField(blank=True)
    cleaned_content = djmodels.TextField(max_length = 500,blank= True)
    cleaned_wordcount = djmodels.IntegerField(blank=True)
    #objects = gazalManager() #GhazalsQueryset.get_cleaned_content()


    def __str__(self):
        return self.ghazal_name

    # class Meta:
    #     ordering =['author_alphabet']


