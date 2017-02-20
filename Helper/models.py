from django.db import models
from django.template.defaultfilters import slugify

TYPE_CHOICES = (
    ('ЗАДВ', 'Задвижка'),
    ('ОК', 'Обратный клапан'),
    ('РЕГ', 'Регулятор'),
    ('Н', 'Насос'),
    ('ТА', 'Турбоагрегат'),
    ('Т/О', 'Теплообменник'),
    ('К', 'Конденсатор'),
    ('КС', 'Конденсатосборник'),
    ('Б', 'Бак'),
    ('ДРЕН', 'Дренаж'),
)


class System(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    short_name = models.CharField(max_length=8, verbose_name='Короткое обозначение')
    info = models.CharField(max_length=250, null=True, blank=True, verbose_name='Описание системы')
    img = models.ImageField(verbose_name='Принципиальная схема', null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.short_name).upper()
        super(System, self).save(*args, **kwargs)

    def __str__(self):
        return '{} - {}'.format(self.short_name, self.name)

    class Meta:
        verbose_name_plural = 'Системы'

class Element(models.Model):
    name = models.CharField(max_length=16, verbose_name='Маркировка')
    info = models.CharField(max_length=200, verbose_name='Название и назначение', blank=True)
    defect = models.CharField(max_length=250, default='Нет дефектов', verbose_name='Дефекты')
    system = models.ForeignKey('System', on_delete=models.CASCADE, null=True, verbose_name='Система элемента')
    type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='ЗАДВ', verbose_name='Тип')
    row = models.CharField(max_length=4, default='А-В', verbose_name='Ряд(ы)')
    axis = models.CharField(max_length=10, default='1-12', verbose_name='Ось(оси)')
    img = models.ImageField(null=True, blank=True,verbose_name='Чертеж,фото,схема')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name).upper()
        super(Element, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Элементы системы'
