from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    created = models.DateField('creation date', auto_now_add=True)
    modify = models.DateField('update date', auto_now=True)
    active = models.BooleanField('Active?', default=True)

    class Meta:
        abstract = True
# classe abstrata serve de rascunho não é criada no BD


class Product(Base):  # Estende de Base
    name = models.CharField('Name', max_length=100)
    price = models.DecimalField('Price',  max_digits=8, decimal_places=2)
    storage = models.IntegerField('Storage')
    image = StdImageField('Image', upload_to='products', variations={
                          'thumb': (124, 124)})  # Titulo  da página na url
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name


"""Função que vai ser realizada antes do save no signal quando Product for salvo, 
Na função dizemos que antes de salvar vai  alterar o slug para a instancia do name"""


def product_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.name)


signals.pre_save.connect(product_pre_save, sender=Product)
