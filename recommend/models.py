from django.db import models
#공고모델 공고정보 pk

#회사모델

#직무 스킬 통계
#스킬 id 매핑 테이블


#다른테이블 속성가져와야하는 클래스는 Model-> Foreign으로 바꾸기
#recruit_info에 포린키 추가함
#jobid는 어떻게?
class recruit_info(models.Model):
    companyId=models.ForeignKey("company",related_name='companyid',on_delete=models.CASCADE,db_column='companyId')
    title=models.CharField(max_length=30)
    #csv에선 job아이디이지만 해당공고 타이틀에 대한 id이므로 titleId로 설정함
    titleId=models.IntegerField()
    job=models.CharField(max_length=30)
    #직무 추천시 사용되는 역량 4가지 skill, task, require, prefer
    skill=models.CharField(max_length=50)
    task=models.CharField(max_length=50)
    require=models.CharField(max_length=50)
    prefer=models.CharField(max_length=50)
    jobUrl=models.CharField(max_length=60)

class company(models.Model):
    companyId=models.IntegerField(primary_key=True)
    company=models.CharField(max_length=30)
    reviewCount=models.IntegerField()
    average=models.IntegerField()
    salary=models.IntegerField()
    wlb=models.IntegerField()
    culture=models.IntegerField()
    possibility=models.IntegerField()
    management=models.IntegerField()

class jobdict(models.Model):
    job=models.CharField(max_length=30)
    python=models.IntegerField()
    java=models.IntegerField()
    javascript=models.IntegerField()

#mainpage에 쓰일 스킬 대분류소분류 테이블 필요하면 엑셀에 정리해서 모델링
#작업하고 사용하기

class skill(models.Model):
    skillId=models.IntegerField(primary_key=True)
    skill=models.CharField(max_length=30)






