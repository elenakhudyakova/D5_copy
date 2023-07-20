
from django.dispatch import receiver
from django.contrib.auth.models import User, Group
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from .views import addpost

@receiver(addpost)
def send_subscribe(instance, category, **kwargs):
    # Если категория для подписчиков существует, вытаскиваю списки и делаю рассылку
    try:
        category_group = Group.objects.get(name=category)
        list_mail = list(User.objects.filter(groups=category_group).values_list('email', flat=True))
        for user_email in list_mail:
            username = list(User.objects.filter(email=user_email).values_list('username', flat=True))[0]
            html_content = render_to_string('subscribe_new_post.html', {'post': instance, 'username': username, 'category': category})
            msg = EmailMultiAlternatives(
                subject=f'News Portal: {category}',
                body='',
                from_email='elkha775@gmail.com',
                to=[user_email, ],
                
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    # Если категории нет (никто еще не подисывался на эту категорию)
    except Group.DoesNotExist:
        pass