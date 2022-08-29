from django.db import models

class Cliente(models.Model):
    apellido:models.CharField(max_length=30)
    nombre:models.CharField(max_length=30)
    balance:models.CharField
    balancef:models.FloatField
    tipoCuenta:models.CharField(max_length=10)
    idCuenta:models.CharField
    dni:models.CharField
    nombreCompleto:models.CharField(max_length=64)
    tarjeta:models.CharField(max_length=16)
    tarjetaUlt:models.CharField(max_length=4)
    img:models.CharField
    tcc:models.BooleanField
    tcg:models.BooleanField
    tcb:models.BooleanField


class Cuenta(models.Model):
    account_id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type_id = models.IntegerField()

    class Meta:
        db_table = 'cuenta'