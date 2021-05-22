from django.db import models


class Search(models.Model):
    # 축척 입력칸
    scale = models.IntegerField()
    # 원하는 이용 면적 입력 칸
    area = models.IntegerField()
    # 이미지 넣는 칸
    Image = models.ImageField(upload_to="input")     # BASE_DIR/media/input 에 저장
