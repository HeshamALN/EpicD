from django.db import models

class Project(models.Model):
    DESIGN = 'Design'
    BUILD = 'Build'
    DESIGNANDBUILD = 'Design & Build'
    CONCEPT = "Concept"

    TASK_CHOICES = [
        (DESIGN, 'Design'),
        (BUILD, 'Build'),
        (DESIGNANDBUILD, 'Design & Build'),
        (CONCEPT, 'Concept'),
    ]

    project_name = models.CharField(max_length=120)
    project_area = models.CharField(max_length=50)
    project_location = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    task_choices = models.CharField(
        max_length=14,
        choices=TASK_CHOICES,
        default=DESIGN,
    )

    project_image = models.ImageField()
    project_image1 = models.ImageField()
    project_image2 = models.ImageField()
    project_image3 = models.ImageField()



    def __str__(self):
        return self.project_name


class About(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=30)
    about = models.TextField(blank=True)
    side_image = models.ImageField()




class Home(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    title1 = models.CharField(max_length=30)
    title2 = models.CharField(max_length=30)
    title3 = models.CharField(max_length=30)
    description1 = models.CharField(max_length=120)
    description2 = models.CharField(max_length=120)
    description3 = models.CharField(max_length=120)
    hiwImage1 = models.ImageField()
    hiwImage2 = models.ImageField()
    hiwImage3 = models.ImageField()
    hiwtitle1 = models.CharField(max_length=30)
    hiwtitle2 = models.CharField(max_length=30)
    hiwtitle3 = models.CharField(max_length=30)
    hiwdescription1 = models.CharField(max_length=120)
    hiwdescription2 = models.CharField(max_length=120)
    hiwdescription3 = models.CharField(max_length=120)
    side_image = models.ImageField()

    # def __str__(self):
    #     return self.image1



