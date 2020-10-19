from django.db import models
class TAddress(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    detail = models.CharField(max_length=100, blank=True, null=True)
    cellphone = models.CharField(max_length=20, blank=True, null=True)
    post_code = models.CharField(max_length=6, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_address'


class TBook(models.Model):
    book_id = models.AutoField(primary_key=True)
    cate = models.ForeignKey('TCates', models.DO_NOTHING, blank=True, null=True)
    book_intrpduce = models.TextField(blank=True, null=True)
    book_photos = models.CharField(max_length=20, blank=True, null=True)
    book_cate = models.IntegerField(blank=True, null=True)
    book_price = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    book_stock = models.CharField(max_length=5, blank=True, null=True)
    print_time = models.DateField(blank=True, null=True)
    revision = models.IntegerField(blank=True, null=True)
    page_count = models.CharField(max_length=20, blank=True, null=True)
    word = models.IntegerField(blank=True, null=True)
    open_type = models.CharField(max_length=20, blank=True, null=True)
    author = models.CharField(max_length=10, blank=True, null=True)
    book_publish = models.CharField(max_length=10, blank=True, null=True)
    book_name = models.CharField(max_length=20, blank=True, null=True)
    pulish_time = models.DateField(blank=True, null=True)
    book_isbn = models.CharField(max_length=100, blank=True, null=True)
    book_wrapper = models.CharField(max_length=100, blank=True, null=True)
    book_dprice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    book_image_path = models.ImageField(upload_to='images')
    shelves = models.DateTimeField(blank=True, null=True)
    customer_socre = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    book_status = models.IntegerField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    menu = models.CharField(max_length=2000, blank=True, null=True)
    author_introduce = models.CharField(max_length=500, blank=True, null=True)
    media_review = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book'

    def func(self):
        return '%.2f'%(self.book_dprice/self.book_price*10)


class TBookOrder(models.Model):
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey('TOrder', models.DO_NOTHING, blank=True, null=True)
    book_numbers = models.IntegerField(blank=True, null=True)
    all_sum = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_book_order'


class TCar(models.Model):
    product_number = models.CharField(max_length=20, blank=True, null=True)
    car_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(TBook, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_car'


class TCates(models.Model):
    cate_id = models.AutoField(primary_key=True)
    cate_name = models.CharField(max_length=10, blank=True, null=True)
    book_numbers = models.CharField(max_length=20, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    cate_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cates'


class TOrder(models.Model):
    order_id = models.CharField(max_length=100,primary_key=True)
    order_time = models.DateTimeField(blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product_numbers = models.CharField(max_length=5, blank=True, null=True)
    address = models.ForeignKey(TAddress, models.DO_NOTHING, blank=True, null=True)
    product_money = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    user = models.ForeignKey('TUser', models.DO_NOTHING, blank=True, null=True)
    zhuangtai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_order'


class TUser(models.Model):
    user_name = models.CharField(max_length=20, blank=True, null=True)
    user_password = models.CharField(max_length=20, blank=True, null=True)
    user_email = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_user'

