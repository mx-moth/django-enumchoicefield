from django import forms
from django.test import SimpleTestCase

from enumchoicefield.enum import PrettyEnum
from enumchoicefield.forms import EnumField, EnumSelect


class MyEnum(PrettyEnum):
    foo = "Foo"
    bar = "Bar"
    baz = "Baz Quux"


class TestEnumForms(SimpleTestCase):

    class EnumForm(forms.Form):
        choice = EnumField(MyEnum)

    def test_enum_field(self):
        form = self.EnumForm()
        self.assertIsInstance(form.fields['choice'].widget, EnumSelect)

    def test_rendering(self):
        form = self.EnumForm()
        html = str(form['choice'])
        self.assertHTMLEqual(html, '\n'.join([
            '<select id="id_choice" name="choice">',
            '<option value="foo">Foo</option>',
            '<option value="bar">Bar</option>',
            '<option value="baz">Baz Quux</option>',
            '</select>',
        ]))

    def test_initial(self):
        form = self.EnumForm(initial={'choice': MyEnum.bar})
        html = str(form['choice'])
        self.assertInHTML('<option value="bar" selected>Bar</option>', html)

    def test_submission(self):
        form = self.EnumForm(data={'choice': 'baz'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['choice'], MyEnum.baz)

    def test_empty_submission(self):
        form = self.EnumForm(data={'choice': ''})
        self.assertFalse(form.is_valid())

    def test_missing_submission(self):
        form = self.EnumForm(data={})
        self.assertFalse(form.is_valid())

    def test_invalid_submission(self):
        form = self.EnumForm(data={'choice': 'nope'})
        self.assertFalse(form.is_valid())


class TestOptionalEnumForms(SimpleTestCase):

    class EnumForm(forms.Form):
        choice = EnumField(MyEnum, required=False)

    def test_enum_field(self):
        form = self.EnumForm()
        self.assertIsInstance(form.fields['choice'].widget, EnumSelect)

    def test_rendering(self):
        form = self.EnumForm()
        html = str(form['choice'])
        self.assertHTMLEqual(html, '\n'.join([
            '<select id="id_choice" name="choice">',
            '<option value="">---------</option>',
            '<option value="foo">Foo</option>',
            '<option value="bar">Bar</option>',
            '<option value="baz">Baz Quux</option>',
            '</select>',
        ]))

    def test_initial(self):
        form = self.EnumForm(initial={'choice': MyEnum.bar})
        html = str(form['choice'])
        self.assertInHTML('<option value="bar" selected>Bar</option>', html)

    def test_submission(self):
        form = self.EnumForm(data={'choice': 'baz'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['choice'], MyEnum.baz)

    def test_empty_submission(self):
        form = self.EnumForm(data={'choice': ''})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['choice'], None)

    def test_missing_submission(self):
        form = self.EnumForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['choice'], None)


class TestComplicatedForm(SimpleTestCase):

    class EnumForm(forms.Form):
        choice = EnumField(MyEnum)
        number = forms.IntegerField()

    def test_valid_form(self):
        form = self.EnumForm(data={'choice': 'foo', 'number': '10'})
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, {'choice': MyEnum.foo, 'number': 10})

    def test_invalid_number(self):
        form = self.EnumForm(data={'choice': 'bar', 'number': 'abc'})
        self.assertFalse(form.is_valid())
        html = str(form['choice'])
        self.assertHTMLEqual(html, '\n'.join([
            '<select id="id_choice" name="choice">',
            '<option value="foo">Foo</option>',
            '<option value="bar" selected>Bar</option>',
            '<option value="baz">Baz Quux</option>',
            '</select>',
        ]))

    def test_invalid_choice(self):
        form = self.EnumForm(data={'choice': 'nope', 'number': '10'})
        self.assertFalse(form.is_valid())
        html = str(form['choice'])
        self.assertHTMLEqual(html, '\n'.join([
            '<select id="id_choice" name="choice">',
            '<option value="foo">Foo</option>',
            '<option value="bar">Bar</option>',
            '<option value="baz">Baz Quux</option>',
            '</select>',
        ]))


class TestLimitedMembers(SimpleTestCase):
    members = [MyEnum.baz, MyEnum.foo]

    def setUp(self):

        class EnumForm(forms.Form):
            choice = EnumField(MyEnum, members=self.members)

        self.EnumForm = EnumForm

    def test_field(self):
        field = EnumField(MyEnum)
        self.assertEqual(field.members, list(MyEnum))

    def test_limited_members(self):
        form = self.EnumForm()
        self.assertEqual(form['choice'].field.members, self.members)
        self.assertHTMLEqual(str(form['choice']), "\n".join([
            '<select name="choice" id="id_choice">',
            '<option value="baz">Baz Quux</option>'
            '<option value="foo">Foo</option>'
            '</select>']))

    def test_invalid_choice(self):
        form = self.EnumForm({'choice': 'bar'})
        self.assertFalse(form.is_valid())

    def test_valid_choice(self):
        form = self.EnumForm({'choice': 'baz'})
        self.assertTrue(form.is_valid())
        self.assertHTMLEqual(str(form['choice']), "\n".join([
            '<select name="choice" id="id_choice">',
            '<option value="baz" selected>Baz Quux</option>'
            '<option value="foo">Foo</option>'
            '</select>']))
