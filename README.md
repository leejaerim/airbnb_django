### 장고 장점
1. model을 정의해주면 장고가 DB소통을 직접 해준다.
2. admin 페이지를 제공해준다.
---
### pyproject.toml
- 다음 파일은, poetry 가상환경에 대한 desc 입니다.

### poetry 설치 [가상환경] Isolation
- `curl -sSL https://install.python-poetry.org | python3 -` 입력
- SSL 에러이슈 
    -> `open /Applications/Python\ 3.7/Install\ Certificates.command` 명령어 입력 으로 SSL 증명서 업데이트
- 환경변수 셋업 .bashrc에 명령어 입력(혹은 ~/.zshrc)

>`poetry.lock` : 패키지의 모든 정보

```python
#init poetry
poetry init
#install django in poetry 
poetry add django
#enter the poetry shell
poetry shell 
#exit the poetry shell
exit
```

### Django
```python
#Command
python ./manage.py runserver
#make migrations 
python manage.py makemigrations
#Migration DB(update DB, sync with django)
python manage.py migrate
#Create Super User
python manage.py createsuperuser
#Create Django app
python manage.py startapp houses
```
- 하나의 app을 별도로 관리합니다. 여러개의 앱이 합쳐져 apps를 만듭니다. 원자성을 보장합니다.
- EX) user, rooms etc...
- models.py에서 모델의 형태를 설정하고 migration을 통해 장고에게 알려줄 수 있다.

### Lecture 6 User
> highly recoomended to set up user Model. in Django Official Docs.
- Django 앱을 할때, custom user를 만드는게 중요하다.
- `from django.contrib.auth.models import AbstractUser` AbstractUser를 상속받아 user를 설계한다.*(프로젝트 user 커스텀)
- `settings.py` 파일에 장고가 user 모델을 사용할 수 있도록 다음과 같이 명시해준다.
```python
AUTH_USER_MODEL = 'users.User' #AppsName.ClassName
```
