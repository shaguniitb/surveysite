from django.db import models
from django.utils.timezone import now

# Create your models here.

class Comment(models.Model):
    text = models.TextField()
    toxicity_score = models.FloatField()
    author = models.CharField(default = 'Test Author', max_length=100)
    author_name = models.CharField(default = 'Test Author', max_length=100)
    pub_date = models.DateField('date published', default = now)
    num_likes = models.IntegerField(default = 0)
    num_comments = models.IntegerField(default = 0)
    num_retweets = models.IntegerField(default = 0)
    url = models.URLField(blank=True, null=True)
    twitter_id = models.CharField(blank=True, null=True, max_length=100)

class Participant(models.Model):

    INTERFACE_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
    )

    username = models.CharField(max_length=100, blank=True, null=True)
    turker_id = models.CharField(max_length=100, blank=True, null=True)
    setting = models.CharField(
        max_length=2,
        choices = INTERFACE_CHOICES,
        default = "1"
        )

    def resetToggle(self):
        toggleSetting, _ = ToggleSetting.objects.get_or_create(participant = self)
        toggleSetting.filter_toxic = False
        toggleSetting.save()

    def resetWordFilter(self):
        wordFilterSetting, _ = WordFilterSetting.objects.get_or_create(participant = self)
        wordFilterSetting.word_filters = ''
        wordFilterSetting.save()       

    def resetIntensitySlider(self):
        sliderSetting, _ = IntensitySliderSetting.objects.get_or_create(participant = self)
        sliderSetting.slider_level = 1
        sliderSetting.save()     

    def resetProportionSlider(self):
        sliderSetting, _ = ProportionSliderSetting.objects.get_or_create(participant = self)
        sliderSetting.slider_level = 1
        sliderSetting.save()                        

class ToggleSetting(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    filter_toxic = models.BooleanField(default = False)

class WordFilterSetting(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    word_filters = models.TextField(blank=True, null=True)

class IntensitySliderSetting(models.Model):

    class SliderChoices(models.IntegerChoices):
      NONE = 1
      A_LITTLE = 2
      SOME = 3
      MORE = 4
      A_LOT = 5

    slider_level = models.IntegerField(
        choices = SliderChoices.choices,
        default = 1
    )
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)

class ProportionSliderSetting(models.Model):

    class SliderChoices(models.IntegerChoices):
      NONE = 1
      A_LITTLE = 2
      SOME = 3
      MORE = 4
      A_LOT = 5

    slider_level = models.IntegerField(
        choices = SliderChoices.choices,
        default = 1
    )
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)    
