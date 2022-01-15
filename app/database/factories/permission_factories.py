import factory
from faker import Faker

from app.models import Permission


fake = Faker()

def _get_permission_name():
    """
    Generate a random permission name.
    The structure of the name is:
    `can-{read|write}-{any|own}-{resource}`
    """
    action = fake.sentence(
        nb_words=2,
        variable_nb_words=False,
        ext_word_list=["read", "write"]
    )
    scope = fake.sentence(
        nb_words=2,
        variable_nb_words=False,
        ext_word_list=["any", "own"]
    )
    resource = fake.sentence(
        nb_words=1,
        variable_nb_words=False,
    )
    permission_name = f"can-{action}-{scope}-{resource}"
    return permission_name
    
    
class RandomPermissionFactory(factory.Factory):
    """
    Class representing a random permission factory.
    Use random data to create random permission.
    The crated permissions follow the next rules:
    `can-{action}-{scope}-{resource}`
    """
    class Meta:
        model = Permission


    permission_name = factory.LazyFunction(_get_permission_name())
    permission_description = factory.Faker("text", max_nb_chars=80)
