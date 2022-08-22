from django.db import models

# Comentamos los models creados que no estaban solicitados en la problematica 1.

""" class AuditoriaCuenta(models.Model):
    old_id = models.IntegerField(blank=True, null=True)
    new_id = models.IntegerField(blank=True, null=True)
    old_balance = models.FloatField(blank=True, null=True)
    new_balance = models.FloatField(blank=True, null=True)
    old_iban = models.CharField(blank=True, null=True)
    new_iban = models.CharField(blank=True, null=True)
    old_type = models.TextField(blank=True, null=True)
    new_type = models.TextField(blank=True, null=True)
    user_action = models.CharField(blank=True, null=True)
    create_at = models.TextField(blank=True, null=True)  # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'auditoria_cuenta' """


class Cliente(models.Model):
    customer_id = models.AutoField()
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(db_column='customer_DNI')  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)  # This field type is a guess.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cliente'


class Cuenta(models.Model):
    account_id = models.AutoField()
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    account_type_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cuenta'


""" class Direccion(models.Model):
    branch_id = models.AutoField(unique=True)
    address_id = models.IntegerField()
    address_text = models.TextField()
    posta_zip = models.TextField()
    city = models.TextField()
    state = models.TextField()
    country = models.IntegerField()
    customer_id = models.IntegerField()
    employee_id = models.IntegerField()
    sucursar_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'direccion' """


class Empleado(models.Model):
    employee_id = models.AutoField()
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(db_column='employee_DNI')  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'empleado'


""" class MarcaTarjeta(models.Model):
    marca_tarjeta_id = models.AutoField(unique=True)
    marca_name = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'marca_tarjeta ' """


class Movimientos(models.Model):
    movimiento_id = models.AutoField(primary_key=True, blank=True, null=True)
    num_cuenta = models.IntegerField(blank=True, null=True)
    monto = models.FloatField(blank=True, null=True)
    tipo = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'movimientos'


class Prestamo(models.Model):
    loan_id = models.AutoField()
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'prestamo'


""" class Sucursal(models.Model):
    branch_id = models.AutoField()
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()
    class Meta:
        managed = False
        db_table = 'sucursal' """


class Tarjeta(models.Model):
    card_id = models.AutoField(primary_key=True)
    card_number = models.IntegerField()
    card_expire = models.IntegerField()
    card_expire_date = models.IntegerField()
    card_cvv = models.IntegerField()
    card_type = models.TextField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tarjeta'

""" 
class TipoCliente(models.Model):
    customer_type_id = models.AutoField(unique=True)
    customer_description = models.IntegerField(blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tipo_cliente '
class TipoCuenta(models.Model):
    account_type_id = models.AutoField()
    account_type_description = models.TextField()
    class Meta:
        managed = False
        db_table = 'tipo_cuenta'
"""