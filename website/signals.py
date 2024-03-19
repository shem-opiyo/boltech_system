from website.models import Course
# import django presave
from  django.db.models.signals import pre_save 
from django.dispatch import receiver 
from django.utils import timezone

@receiver(pre_save, sender=Course)
def course_pre_save(sender, instance, **kwargs):
    # lets append the current time to the image of the course as image-name-YEAR-MONTH-DAY-HOUR-MINUTE.ext

    if not instance.pk:
        # this is a new course
        image_name = instance.image.name.split(".")[0]
        image_ext = instance.image.name.split(".")[1]
        instance.image.name = f"{image_name}-{timezone.now().strftime('%Y-%m-%d-%H-%M')}.{image_ext}"
        print(f"===== New course image name: {instance.image.name}")
    else:
        # this is an existing course
        old_course = Course.objects.filter(pk=instance.pk).first()
        if not old_course:
            return
        if old_course.image != instance.image:
            # the image has changed
            image_name = instance.image.name.split(".")[0]
            image_ext = instance.image.name.split(".")[1]
            instance.image.name = f"{image_name}-{timezone.now().strftime('%Y-%m-%d-%H-%M')}.{image_ext}"
            print(f"===== New course image name: {instance.image.name}")
        else:
            print("===== Image has not changed")


