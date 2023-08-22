# Generated by Django 4.2.4 on 2023-08-21 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_alter_member_member_role_alter_member_member_status'),
        ('static_app', '0003_badge_badge_image_badge_category'),
        ('neulhaerang', '0003_alter_neulhaerangreply_donation_neulhaeranglike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businessplan',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='byeoljji',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='memberbyeoljji',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
        migrations.AlterField(
            model_name='memberbyeoljji',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='neulhaerang',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='static_app.category'),
        ),
        migrations.AlterField(
            model_name='neulhaerang',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
        migrations.AlterField(
            model_name='neulhaerangdonation',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
        migrations.AlterField(
            model_name='neulhaerangdonation',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='neulhaeranginnercontent',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='neulhaeranginnerphotos',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='neulhaeranginnertitle',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='neulhaeranglike',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
        migrations.AlterField(
            model_name='neulhaeranglike',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='neulhaerangparticipants',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
        migrations.AlterField(
            model_name='neulhaerangparticipants',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='neulhaerangreply',
            name='donation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerangdonation'),
        ),
        migrations.AlterField(
            model_name='neulhaerangreply',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
        migrations.AlterField(
            model_name='neulhaerangreply',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='neulhaerangtag',
            name='neulhaerang',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerang'),
        ),
        migrations.AlterField(
            model_name='replylike',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.member'),
        ),
        migrations.AlterField(
            model_name='replylike',
            name='neulhaerang_reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='neulhaerang.neulhaerangreply'),
        ),
    ]