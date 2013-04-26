class Person:
    """Model of a person with parents and children."""

    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.mother = mother
        if mother is not None:
            self.mother._children.append(self)

        self.father = father
        if father is not None:
            self.father._children.append(self)

        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self._children = []

    def children(self, gender=None):
        """Return all children of this person, optionally filtered by gender"""
        return [child for child in self._children
                if gender is None or child.gender == gender]

    def _get_siblings(self, gender=None):
        """Return all siblings of this person.

        Siblings are considered to be people with at least one common parent
        """
        siblings_list = []

        if self.mother is not None:
            siblings_list.extend(self.mother.children(gender=gender))

        if self.father is not None:
            siblings_list.extend(self.father.children(gender=gender))

        siblings = set(siblings_list)

        if self in siblings:
            siblings.remove(self)

        return siblings

    def get_brothers(self):
        """Return a list of all brothers of this person.

        Brothers are all people with at least one common parent and gender='M'
        """
        return list(self._get_siblings(gender='M'))

    def get_sisters(self):
        """Return a list of all sisters of this person.

        Sisters are all people with at least one common parent and gender='F'
        """
        return list(self._get_siblings(gender='F'))

    def is_direct_successor(self, person):
        """Check if `person` is a child of this person."""
        return person in self._children
