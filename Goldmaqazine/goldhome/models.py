from django.db import models
from django.urls import reverse
from phonenumber_field.modelfields import PhoneNumberField



class Phone(models.Model):
    name = models.CharField(max_length=50, verbose_name='Adiniz')
    #phone = PhoneNumberField(verbose_name='Telefon nomreniz',region='AZ',blank=True)




class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='Adi')
    message = models.TextField(verbose_name='Mesajiniz')
    email = models.EmailField(max_length=70, verbose_name="Email")
    date_at = models.DateTimeField(auto_now_add=True, verbose_name='Qeyd tarixi')
    #phone = PhoneNumberField(verbose_name='Telefon nomreniz',region='AZ',blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Mektublar'




class Category(models.Model):
    title = models.CharField(max_length=50,null=True,verbose_name='Katiqoriya')
    post_title = models.CharField(max_length=50,null=True,verbose_name='Novu')
    slug = models.SlugField(max_length=50,unique=True, null=True)
    image = models.ImageField(upload_to='imagecat/%Y/%m/%d/', verbose_name='KatSəkil')


    def get_absalute_url(self):
        return reverse('category', kwargs={'category_id': self.category_id})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Katiqoriya'
        verbose_name_plural = 'Katiqoriyalar'




class Tag(models.Model):
    title = models.CharField(max_length=50,null=True,verbose_name='Adlari')
    slug = models.SlugField(max_length=50,unique=True,null=True)


    def get_absalute_url(self):
        return reverse('tag_detail', kwargs={'tag_slug': self.slug,})


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Nov'
        verbose_name_plural = 'Novler'




class Gold(models.Model):
    title = models.CharField(max_length=50, verbose_name='Məhsulun adı')
    category = models.ForeignKey(Category, null=True,on_delete=models.DO_NOTHING, verbose_name="Katiqoriya")
    tags = models.ManyToManyField(Tag,blank=True, verbose_name='Secim novu',)
    post_title = models.CharField(max_length=50, null=True, verbose_name='Modeli')
    image = models.ImageField(upload_to='image/%Y/%m/%d/',verbose_name='Səkil',blank=True)
    probe = models.IntegerField(null=True, blank=True, verbose_name='Probu')
    weight = models.FloatField(null=True, blank=True, verbose_name='Çəkisi')
    price = models.FloatField(null=True, blank=True,verbose_name='Qiyməti AZN')
    creded_at = models.DateTimeField(auto_now_add=True, verbose_name='Qeyd tarixi')
    creded_up = models.DateTimeField(auto_now=True, verbose_name='Yenilenme tarixi')
    public = models.BooleanField(default=True, verbose_name='Dərc edilib')
    email = models.EmailField(max_length=70,blank=True, verbose_name="Email")



    def get_absalute_url(self):
        return reverse('post', kwargs={'get_id': self.pk})


    def __str__(self):
        return self.title


    class Meta:

        verbose_name = 'Qizil'
        verbose_name_plural = 'Qizillar'
        ordering = ['-creded_at']




class Carusel(models.Model):
    name = models.CharField(max_length=50, verbose_name='Carusel adi')
    title = models.CharField(max_length=50, verbose_name='Məhsulun adı')
    content = models.TextField(blank=True, verbose_name='Yenilikler haqqinda')
    image = models.ImageField(upload_to='carusel_image/%Y/%m/%d/',verbose_name='Carusel Səkil',blank=True)
    price = models.FloatField(null=True, blank=True, verbose_name='Qiyməti AZN')
    creded_at = models.DateTimeField(auto_now_add=True, verbose_name='Qeyd tarixi',blank=True)
    public = models.BooleanField(default=True, verbose_name='Dərc edilib')



    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Carusel'
        verbose_name_plural = 'Carusel haqda'
        ordering = ['-creded_at']

