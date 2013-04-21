class Person:
    """Model of a person with parents and children."""

    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self._mother = None
        self._father = None

        self.name = name
        self.birth_year = birth_year
        self.gender = gender

        if mother is not None:
            self.mother = mother
        if father is not None:
            self.father = father

        self._children = set()

    @property
    def mother(self):
        return self._mother

    @mother.setter
    def mother(self, new_mother):
        """Set mother, removing the connection to a previous one."""
        del self.mother

        if self.birth_year - new_mother.birth_year < 18:
            raise ValueError("The parent must be at least 18 years older "
                             "than the child")

        self._mother = new_mother
        self._mother._children.add(self)

    @mother.deleter
    def mother(self):
        """Remove the connection to the mother."""
        if self._mother is not None:
            self._mother._children.remove(self)

        self._mother = None

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, new_father):
        """Set father, removing the connection to a previous one."""
        del self.father

        if self.birth_year - new_father.birth_year < 18:
            raise ValueError("The parent must be at least 18 years older "
                             "than the child")

        self._father = new_father
        self._father._children.add(self)

    @father.deleter
    def father(self):
        """Remove the connection to the father."""
        if self._father is not None:
            self._father._children.remove(self)

        self._father = None

    def children(self, gender=None):
        """Return all children of this person, optionally filtered by gender"""
        if gender is not None:
            return [child for child in self._children
                    if child.gender == gender]
        else:
            return list(self._children)

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
