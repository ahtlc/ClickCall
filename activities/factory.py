from calls.models import Call,Contact,Subject,Tag
from faker import Faker
import factory
import factory.django
import factory.fuzzy
import pytz
from calls import models
from django.http import HttpResponse

fake = Faker()

import datetime
STATUS_IDS = [x[0] for x in Contact.STATUS_CHOICES]
class ContactFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Contact
    name = factory.Faker('name')
    company_name = factory.Faker('company')
    email = factory.Faker('email')
    cellphone = fake.numerify(text="(##)#-####-####")
    phone =  fake.numerify(text="(##)####-####")
    adress = factory.Faker('address')
    last_update = factory.fuzzy.FuzzyDateTime(datetime.datetime(2017, 1, 1, tzinfo=pytz.timezone('UTC')))
    status = factory.fuzzy.FuzzyChoice(STATUS_IDS)
    @factory.post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return
        if extracted:
            self.tag.add(extracted)

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag
    name = 'Tag Inicial'

class SubjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subject
    name = factory.fuzzy.FuzzyText(length=12)

class CallFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Call
    duration = datetime.datetime.now().time()
    call_24_hours = fake.pybool()
    email_sended = fake.pybool()
    paid = fake.pybool()
    contact = factory.Iterator(models.Contact.objects.all())
    notes = fake.text()
    date = factory.fuzzy.FuzzyDate(datetime.date(2009, 1, 1))
    @factory.post_generation
    def subjects(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            self.subject.add(extracted)

def create():
    print('Tags:')
    tagV = ['pessoa', 'empresa', 'socio']
    if(len(Tag.objects.all())==0):
        for i in range(3):
            tag = Tag()
            tag.name = tagV[i]
            tag.save()

    else:
        print('tag ja criada')
    print('Contatos:')
    for i in range(10):
        contact = ContactFactory.create(tags = factory.Iterator(models.Tag.objects.all()))
        print(contact)
    print('Assuntos:')
    for i in range(10):
        subject = SubjectFactory.create()
        print(subject)
    print('Calls:')
    for i in range(200):
        created = CallFactory.create(subjects = factory.Iterator(models.Subject.objects.all()))
        print(created.date)
    return HttpResponse("Seu banco de dados está populado por XxAvengeDxX(add la no lol) - Marquinho Hacker")