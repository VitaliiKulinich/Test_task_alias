from django.test import TestCase
from alias.models import Alias, create_an_alias, get_aliases, alias_replace
from datetime import datetime

# Create your tests here.
class SomeTest(TestCase):
    def test_creation_first_record_in_db(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        self.assertEqual(my_alias.alias, "1_alias")
        self.assertEqual(my_alias.target, "1_target")
        self.assertEqual(my_alias.start, datetime(2020, 1, 1, 0, 0, 0, 0))
        self.assertEqual(my_alias.end, datetime(2020, 2, 1))

    def test_creation_two_equal_records(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        self.assertEqual(len(Alias.objects.all()), 1)

    def test_creation_record_with_already_used_alias(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="2_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        self.assertEqual(len(Alias.objects.all()), 1)

    def test_creation_two_different_aliases(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias2 = create_an_alias(
            alias="2_alias",
            target="2_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        self.assertEqual(len(Alias.objects.all()), 2)

    def test_creation_two_records_with_the_same_alias_and_records_but_different_time(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 3, 1, 0, 0, 0, 0),
            end=datetime(2020, 4, 1, 0, 0, 0, 1),
        )
        self.assertEqual(len(Alias.objects.all()), 2)

    def test_creation_three_records_with_the_same_alias_and_records_but_different_time(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 3, 1, 0, 0, 0, 0),
            end=datetime(2020, 4, 1, 0, 0, 0, 1),
        )
        my_alias3 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 5, 1, 0, 0, 0, 0),
            end=datetime(2020, 6, 1, 0, 0, 0, 1),
        )
        self.assertEqual(len(Alias.objects.all()), 3)

    def test_creation_two_correct_records_and_one_not(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 3, 1, 0, 0, 0, 0),
            end=datetime(2020, 4, 1, 0, 0, 0, 1),
        )
        my_alias3 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        self.assertEqual(len(Alias.objects.all()), 2)

    def test_creation_records_with_end_None(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=None,
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 3, 1, 0, 0, 0, 0),
            end=datetime(2020, 4, 1, 0, 0, 0, 1),
        )
        my_alias3 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        self.assertEqual(len(Alias.objects.all()), 1)

    def test_get_unexisting_aliases(self):
        result = get_aliases(
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 6, 1, 0, 0, 0, 0),
        )
        self.assertFalse(result)

    def test_get_three_aliases(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 3, 1, 0, 0, 0, 0),
            end=datetime(2020, 4, 1, 0, 0, 0, 1),
        )
        my_alias3 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 5, 1, 0, 0, 0, 0),
            end=datetime(2020, 6, 1, 0, 0, 0, 1),
        )
        result = get_aliases(
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 6, 1, 0, 0, 0, 0),
        )
        self.assertEqual(len(result["1_alias"]), 3)

    def test_get_two_aliases_and_one_with_None_end_1(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 6, 1, 0, 0, 0, 0),
            end=None,
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias3 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 3, 1, 0, 0, 0, 0),
            end=datetime(2020, 4, 1, 0, 0, 0, 1),
        )
        result = get_aliases(
            target="1_target", start=datetime(2020, 1, 1, 0, 0, 0, 0), end=None
        )
        self.assertEqual(len(result["1_alias"]), 3)

    def test_get_one_aliases_and_one_with_None_end_1(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 6, 1, 0, 0, 0, 0),
            end=None,
        )
        my_alias2 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        my_alias3 = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 3, 1, 0, 0, 0, 0),
            end=datetime(2020, 4, 1, 0, 0, 0, 1),
        )
        result = get_aliases(
            target="1_target", start=datetime(2020, 3, 1, 0, 0, 0, 0), end=None
        )
        self.assertEqual(len(result["1_alias"]), 2)

    def test_replace_unexisting_alias(self):
        replaced = alias_replace(
            existing_alias="1_alias",
            replace_at=datetime(2020, 3, 1, 0, 0, 0, 0),
            new_alias_value="2_alias",
        )
        self.assertFalse(replaced)

    def test_replace_existing_alias(self):
        my_alias = create_an_alias(
            alias="1_alias",
            target="1_target",
            start=datetime(2020, 1, 1, 0, 0, 0, 0),
            end=datetime(2020, 2, 1, 0, 0, 0, 1),
        )
        replaced = alias_replace(
            existing_alias="1_alias",
            replace_at=datetime(2020, 3, 1, 0, 0, 0, 0),
            new_alias_value="2_alias",
        )
        self.assertEqual(replaced, "2_alias")
