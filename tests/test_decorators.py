import graphene

from graphene_validator.decorators import validated
from .validation_test_suite import InputForTests, PersonalData, ValidationTestSuite


class OutputForTests(graphene.ObjectType):
    email = graphene.String()
    the_person = graphene.Field(PersonalData)


@validated
class DecoratorMutation(graphene.Mutation):
    class Arguments:
        _inpt = graphene.Argument(InputForTests, name="input")

    Output = OutputForTests

    def mutate(self, _info, _inpt=None):
        if _inpt is None:
            _inpt = {}

        return OutputForTests(
            email=_inpt.get("email"),
            the_person=_inpt.get("the_person"),
        )


class Mutations(graphene.ObjectType):
    test_mutation = DecoratorMutation.Field()


class TestDecorators(ValidationTestSuite):
    schema = graphene.Schema(mutation=Mutations)