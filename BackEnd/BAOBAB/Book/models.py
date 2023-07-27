from django.db import models

class BookInfo(models.Model):
    book_id = models.AutoField(primary_key=True)
    mainCategory = models.ForeignKey()
    subCategory = models.ForeignKey()

    book_Name = models.CharField(max_length=255)
    author = models.CharField(max_length=20)
    is_popular = models.BooleanField(default=False)
    publication_year = models.CharField(max_length=20)
    publication_month = models.CharField(max_length=10)

    def __str__(self):
        return self.book_Name


class BookFile(models.Model):
    book_id = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    book_file = models.FileField()


class BookCover(models.Model):
    book_id = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    book_cover = models.ImageField()


class BookStats(models.Model):
    book_id = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    
    rating = models.FloatField(default=0.0)
    liked = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
