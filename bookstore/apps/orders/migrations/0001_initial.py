# Generated by Django 5.2.1 on 2025-06-05 02:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Họ và tên')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Số điện thoại')),
                ('address', models.TextField(verbose_name='Địa chỉ')),
                ('city', models.CharField(max_length=50, verbose_name='Thành phố')),
                ('district', models.CharField(max_length=50, verbose_name='Quận/Huyện')),
                ('ward', models.CharField(max_length=50, verbose_name='Phường/Xã')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Tổng tiền')),
                ('shipping_fee', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Phí vận chuyển')),
                ('payment_method', models.CharField(choices=[('cod', 'Thanh toán khi nhận hàng')], default='cod', max_length=20, verbose_name='Phương thức thanh toán')),
                ('status', models.CharField(choices=[('pending', 'Chờ xử lý'), ('confirmed', 'Đã xác nhận'), ('shipping', 'Đang giao hàng'), ('delivered', 'Đã giao hàng'), ('cancelled', 'Đã hủy')], default='pending', max_length=20, verbose_name='Trạng thái')),
                ('notes', models.TextField(blank=True, verbose_name='Ghi chú')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Ngày tạo')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Ngày cập nhật')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Đơn hàng',
                'verbose_name_plural': 'Đơn hàng',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(verbose_name='Số lượng')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Giá')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.order')),
            ],
            options={
                'verbose_name': 'Chi tiết đơn hàng',
                'verbose_name_plural': 'Chi tiết đơn hàng',
            },
        ),
    ]
