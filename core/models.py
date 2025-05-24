from django.db import models

class Apoio(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Apoio de {self.nome}"

class Voluntariado(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    disponibilidade = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voluntário {self.nome}"

class Transparencia(models.Model):
    ano_anterior = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    ano_atual = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    meta_doacoes = models.DecimalField(max_digits=10, decimal_places=2, default=0)

class Gasto(models.Model):
    item = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=10, decimal_places=2)