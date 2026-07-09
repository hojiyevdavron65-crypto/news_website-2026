from modeltranslation.translator import register,TranslationOptions
from .models import Article,Category,Tag

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields=('title','body','slug')


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields=('name',)

@register(Tag)
class TagTranslationOptions(TranslationOptions):
    fields=('name',)