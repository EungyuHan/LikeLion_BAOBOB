from django.db import models

class Category(models.Model){
    category_name = models.CharField(max_length=255, primary_key=True)
    mainCategory_name = models.Foreignkey(Category, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False)
}