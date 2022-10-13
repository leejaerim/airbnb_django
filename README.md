### 장고 장점
1. model을 정의해주면 장고가 DB소통을 직접 해준다.
2. admin 페이지를 제공해준다.
---
### pyproject.toml
- 다음 파일은, poetry 가상환경에 대한 desc 입니다.

> `dir` method을 통해 해당 오브젝트가 가진 속성을 확인 할 수 있다.

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
#ImageFields를 사용하기 위한 Pillrow 설치
poetry add Pillrow
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
- models.py를 변경할때마다 migration 및 migrate를 해야 합니다. -> DB와 장고의 동기화
### RelationShip in Django
- 서로 다른 App간 대화.
`Owner = models.ForeignKey("users.User",on_delete=models.CASCADE)`  

### Shell Control with ORM
> .all(), .filter(), .get(), create(), delete()
```python
Room.object.all()
Room.object.get(name="TEST_")

# => Error get must be retruning 1 object
Room.objects.filter(pet_friendly=True)

Room.object.filter(price__gt=15)
Room.object.filter(name__contains="서울")
#create
Amenity.object.create(name="Amenity Test", description="How Cool is this.!")
#delete
to_delete = Amenity.objects.get(pk=7)
to_delete.delete() 
```

### What is the QuerySet
- `Room.objects.filter(pet_friendly=True).exclude(price__lt=15).filter(name__contains="서울")`
> Roles in QuerySet -> provide Lazy Chainng operations, when they needs an actual data.

### Reverse accsessor
-  when create foreignkey, that models added *_set model . 
- that is , how you access reverse.

### 장고 템플릿의 한계
- 브라우저 자바스크립트, 즉 리액트를 이용해 동적으로 보여주길 원함.
- html 이상 동적으로 보여주기엔 템플릿은 한계가 존재.
- 장고는 admin 패널과 ORM , react를 제공하기 위한 API 사용

### serializer 
- python 객체를 JSON으로 직렬화.
- rest_framework를 좀더 유연하게 사용하도록 함.
- serializer validation 제공.

### DRF
- `Router` url 과 viewset을 좀더 유연하게 작성하게 해줌
- 