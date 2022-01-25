from faker import Faker


fake = Faker()

def get_permission_name() -> str:
    """
    Generate a random permission name.
    The structure of the name is:
    `can-{read|write}-{any|own}-{resource}`
    """
    action = fake.sentence(
        nb_words=1,
        variable_nb_words=False,
        ext_word_list=["read", "write"]
    ).lower().strip(".")
    scope = fake.sentence(
        nb_words=1,
        variable_nb_words=False,
        ext_word_list=["any", "own"]
    ).lower().strip(".")
    resource = fake.sentence(
        nb_words=1,
        variable_nb_words=False,
    ).lower().strip(".")
    permission_name = f"can-{action}-{scope}-{resource}"
    return permission_name
