# The process will go through different functions and classes to determine based on what Alleles of the parents, will the child get which blood group
# Then the data will be visualised using rich as it is the lightest CLI-based visualization framework out there and its in ASCII so it does not rely on the web.

import re
import random
from rich.console import Console
from rich.live import Live
from time import sleep


# person class will crate a person object to determine their alleles, the class init itself, and the random choice of alleles based on
# probabalistic weights converted from the ABO antigen system, the explanation of which is below:-
# Parent 1: AO, Parent 2: OO -> Child: A (A is dominant, O is recessive)
# Parent 1: BO, Parent 2: OO -> Child: B (B is dominant, O is recessive)
# Child has a 50-50 chance of inheriting A or B if one parent has OO

class Person:
    def __init__(self, parent1=None, parent2=None):
        self.parent1 = parent1
        self.parent2 = parent2
        self.blood_type, self.rh = self.assign_blood_type_and_rh()

    # calling the possible_child_blood_types function to determine Rh and alleles instead of doing it manually in two places
    def assign_blood_type_and_rh(self):
        if self.parent1 and self.parent2:
            # print(f"Parent1: {self.parent1.blood_type}{self.parent1.rh}, Parent2: {self.parent2.blood_type}{self.parent2.rh}") debug statement
            possible_blood_types = possible_child_blood_types(
                self.parent1.blood_type, self.parent2.blood_type,
                self.parent1.rh, self.parent2.rh
            )
            # debug statement: print(f"Possible child blood types: {possible_blood_types}")
            chosen_type = random.choice(possible_blood_types)
            return chosen_type[:-1], chosen_type[-1]
        else:
            return self.random_allele(), self.random_rh()

    @staticmethod
    def random_allele():
        return random.choices(["A", "B", "O"], weights=[45, 45, 10], k=1)[0]

    @staticmethod
    def random_rh():
        return random.choice(["+", "-"])


# this function will 
def parse_alleles(bg):

    """ Checks user input for the correct allele when called in main for each allele, AB, B, A, and O takes input of str bg as input """

    if "AB" in bg:
        return ["A", "B"]
    elif "B" in bg:
        return ["B", "B"]
    elif "A" in bg:
        return ["A", "A"]
    elif "O" in bg:
        return ["O", "O"]
    else:
        raise ValueError("Invalid blood group format.")


# 
def possible_child_blood_types(parent1_bg, parent2_bg, parent1_rh, parent2_rh):

    """ In the dict we have keys as tuples and the values are lists we used tuples because they represent a PAIR of parent blood types and lists
            are used to represent the possible blood group types for the child """

    # print(f"Checking combinations for: {parent1_bg}, {parent2_bg}") debug comment, use when needed
    blood_type_combinations = {
        ("A", "A"): ["A", "O"],
        ("A", "B"): ["A", "B", "AB", "O"],
        ("A", "AB"): ["A", "B", "AB"],
        ("A", "O"): ["A", "O"],
        ("B", "B"): ["B", "O"],
        ("B", "AB"): ["A", "B", "AB"],
        ("B", "O"): ["B", "O"],
        ("AB", "AB"): ["A", "B", "AB"],
        ("AB", "O"): ["A", "B"],
        ("O", "O"): ["O"],
    }

    # check both possible orders, cause ("B", "A") can be ("A", "B") but it must still match ["A", "B", "AB", "O"] using a conditional statement.
    # use the normalize concept to sort the keys and normalizing the tuple
    abo = blood_type_combinations.get((parent1_bg, parent2_bg)) or blood_type_combinations.get((parent2_bg, parent1_bg), [])

    # print(f"Possible ABO combinations: {abo}") debug comment, use when needed.

    # determining the Rh inheritance as well (Rh is '+' or '-' antigens with the blood group)
    rh = []
    for rh1 in parent1_rh:
        for rh2 in parent2_rh:
            if "+" in (rh1, rh2):
                rh.append("+")
            else:
                rh.append("-")

    # get rid of duplicate blood groups to avoid confusion and combine ABO and Rh algorithms
    rh = list(set(rh))
    possible_bg = [f"{abo_}{rh_}" for abo_ in abo for rh_ in rh]

    return possible_bg


# main function that will take user input for their parents blood groups to be passed into the blood group app class
def main():

    # getting the user input until they get it right or they can quit using ctrl+c
    while True:
        try:
            parent1_blood_group = input("Enter the blood group of parent 1: ").strip()
            parent2_blood_group = input("Enter the blood group of parent 2: ").strip()

            # using string slicing to get rid of the + and - antigens only to use regex for the blood group alleles
            if parent1_blood_group[-1] in "+-":
                parent1_rh = parent1_blood_group[-1]
                parent1_blood_group = parent1_blood_group[:-1]
            else:
                raise ValueError("Invalid blood group format.")

            if parent2_blood_group[-1] in "+-":
                parent2_rh = parent2_blood_group[-1]
                parent2_blood_group = parent2_blood_group[:-1]
            else:
                raise ValueError("Invalid blood group format.")

            # using regex to compile the captured group and error checking for correct format, raising ValueError for incorrect format
            blood_group_pattern = re.compile(r"^(A|B|O|AB)$")
            if not blood_group_pattern.match(parent1_blood_group) or not blood_group_pattern.match(parent2_blood_group):
                raise ValueError("Invalid blood group format. Please enter A+, A-, B+, B-, AB+, AB-, O+, or O- or exit with 'ctrl+c'")

            # initializing the Person object with each of the parent's blood groups with alleles and antigens separately
            parent1 = Person()
            parent1.blood_type = parent1_blood_group
            parent1.rh = parent1_rh

            parent2 = Person()
            parent2.blood_type = parent2_blood_group
            parent2.rh = parent2_rh

            # initializing the child object on parent1 and parent2
            child = Person(parent1, parent2)

            # calling the visualizing function if all conditions are satisfied
            visualize_family_tree(child, parent1, parent2)
            break

        except ValueError as e:
            print(e)
            continue

# function that uses the "Rich" ASCII framework to animate the relational output of the parent blood groups that point to the possible
# child blood group
def visualize_family_tree(child, parent1, parent2):
    """Generate an animated upside down eert in ASCII"""

    # if there is no child value given to the function then return nothing
    if child is None:
        return ""

    # initialize the console object as per Rich documentation
    console = Console()

    # animation frames that will hopefully simulate a tree growing upside down (it's going to be a list of lists)
    # first show alleles of parent1, then show p1+p2 then start forming and upside down eert to
    frames = [
        [
            "   ",
            "     ",
            "      ",
            "       ",
            "        ",
        ],
        [
            f"   {parent1.blood_type}{parent1.rh}",
            "     ",
            "      ",
            "       ",
            "        ",
        ],
        [
            f"   {parent1.blood_type}{parent1.rh}         {parent2.blood_type}{parent2.rh}",
            "     ",
            "      ",
            "       ",
            "        ",
        ],
        [
            f"   {parent1.blood_type}{parent1.rh}         {parent2.blood_type}{parent2.rh}",
            "     \\       /",
            "      ",
            "       ",
            "        ",
        ],
        [
            f"   {parent1.blood_type}{parent1.rh}         {parent2.blood_type}{parent2.rh}",
            "     \\       /",
            "      \\     /",
            "       ",
            "        ",
        ],
        [
            f"   {parent1.blood_type}{parent1.rh}         {parent2.blood_type}{parent2.rh}",
            "     \\       /",
            "      \\     /",
            "       \\   /",
            f"         {child.blood_type}{child.rh}",
        ],
    ]

    # animating the tree
    with Live("", console=console, refresh_per_second=2) as live:
        for frame in frames:
            # this line updates the tree frames after a new line for each list in the list
            live.update("\n".join(frame))
            sleep(1.0)

    # printing the animation along wiht a reasoning statement, with the condition that "if parent 1 had a certain set of alleles and parent 2 had a certain set
    # of alleles and out of those if there is either A or B in either parent,
    # that will get chosen as it is dominant if they also had O. Otherwise if they had any combination of A and B alleles,
    # they both have a 50-50 chance of being inherited"
    dominant_alleles = []
    for allele in parent1.blood_type + parent2.blood_type:
        if allele in ["A", "B"]:
            dominant_alleles.append(allele)

    if not dominant_alleles:
        dominant_alleles = ["O"]

    # printing the reasoning statement
    console.print(
        f"[bold red]Based on the ABO antigen system of determining blood type:[/bold red] parent 1 had: {parent1.blood_type}{parent1.rh} and parent 2 had: {parent2.blood_type}{parent2.rh} out of which, {' and '.join(dominant_alleles)} alleles are dominant."
    )
    # print the final upside down tree for static visual ascii picture
    console.print("\n".join(frames[-1]))

if __name__ == "__main__":
    main()
