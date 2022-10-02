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
#Migration DB
python manage.py migrate
#Create Super User
python manage.py createsuperuser
#Create Django app
python manage.py startapp houses
```
- 하나의 app을 별도로 관리합니다. 여러개의 앱이 합쳐져 apps를 만듭니다. 원자성을 보장합니다.
- EX) user, rooms etc...
