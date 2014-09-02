"""TestCase for conceptual tests.

ConceptTestCases are designed to be natural language tests that help
students understand high-level understanding. As such, these test cases
focus mainly on unlocking. When used in the grading protocol,
ConceptTestCases simply display the answer if already unlocked.
"""

from models import core
from models import serialize
from protocols import grading
from protocols import unlock
import utils

class ConceptCase(grading.GradedTestCase, unlock.UnlockTestCase):
    """TestCase for conceptual questions."""

    type = 'concept'

    REQUIRED = {
        'type': serialize.STR,
        'question': serialize.STR,
        'answer': serialize.STR,
    }
    OPTIONAL = {
        'locked': serialize.BOOL_TRUE,
        'choices': serialize.SerializeArray(serialize.STR),
    }

    ######################################
    # Protocol interface implementations #
    ######################################

    def on_grade(self, logger, verbose, interact):
        """Implements the GradedTestCase interface."""
        if verbose:
            utils.underline('Concept question', line='-')
            print(self['question'])
            print('A: ' + self['answer'])
            print()
        return False

    def should_grade(self):
        return not self['locked']

    def on_unlock(self, logger, interact_fn):
        """Implements the UnlockTestCase interface."""
        print(self['question'])
        answer = interact_fn(self['answer'], self['choices'])
        self['answer'] = answer
