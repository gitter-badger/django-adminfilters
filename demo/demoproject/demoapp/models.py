from django.db import models

class DemoRelated(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class DemoModel(models.Model):
    name = models.CharField(max_length=255)
    demo_related = models.ForeignKey('DemoRelated')

    class Meta:
        app_label = 'demoapp'

class DemoModel_RelatedFieldCheckBoxFilter(DemoModel):
    class Meta:
        proxy = True
        verbose_name = "RelatedFieldCheckBoxFilter"

class DemoModel_RelatedFieldRadioFilter(DemoModel):
    class Meta:
        proxy = True
        verbose_name = "RelatedFieldRadioFilter"

class DemoModel_UnionFieldListFilter(DemoModel):
    class Meta:
        proxy = True
        verbose_name = "UnionFieldListFilter"

class DemoModel_IntersectionFieldListFilter(DemoModel):
    class Meta:
        proxy = True
        verbose_name = "IntersectionFieldListFilter"
