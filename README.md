# Blood Group Inheritance

## Description

This program generates an animation of a reverse ASCII tree for visualizing the probability of assigning a possible blood group for a child, given the user input of their parent's blood groups. The program has 4 functions total.

It has one `main` function, and three purposeful functions:
1. One for calculating the algorithm of the blood group and antigen assignment
2. One for error checking of blood group correction when user input is given to parse each parent's alleles
3. One function that generates the ASCII tree animation at the terminal

This program generates a child's blood group from what their parent's alleles are, based on the ABO antigen system discovered by the Austrian pathologist and biologist [Karl Landsteiner](https://en.wikipedia.org/wiki/Karl_Landsteiner) in 1901. Blood types are classified into type A, type B, type AB, and type O based on five glycoprotein antigens-A, B, AB, A1, and H-that are expressed on the surface of RBCs along with the Rh antigen system for + and - antigens.

The process will go through different functions and classes to calculate which blood group the child will get based on the parents' alleles. Then the data will be visualized using [Rich](https://rich.readthedocs.io/en/stable/introduction.html) as it is the lightest visualization framework available, and its ASCII output doesn't rely on the web, APIs, or any variable framework that generates files, which reduces the probability of running into issues.

I chose this topic because it's important and useful to me personally. I'm fascinated with Microbiology and Genetic Engineering and hope to contribute to that field someday by graduating and/or enrolling for a higher level degree program. I also wanted to have useful methods of manipulating biological data by determining what data structures to use programmatically. It is part of a bigger project that I am working on which encorporates a MUCH larger framework, and it's main target is to standardize the data structures that are used for certain biotechnical/biomedical engineering applications like **genetic sequence parsing algorithms** and simpler algorithms like a blood group determiner. An example is how this fundamental idea and algorithm was used in my [Bloodlink](https://github.com/Hdave00/bloodlink) project.
The program:
- Takes user input for parent's blood groups
- Parses the alleles and antigens
- Runs the data through an algorithm to determine inheritance of both:
  - The ABO system for alleles
  - The Rh system for "+" and "-" antigens

## Table of Contents

1. [Functions, Classes, Unit Testing](#1-functions-classes-unit-testing-and-explanation)
2. [Installation](#2-installation)
3. [Usage](#3-usage)
4. [Sources and Links](#4-sources-and-links)

### 1. Functions, Classes, Unit Testing and Explanation

There are 3 core functions: `parse_alleles`, `possible_child_blood_types` and `visualize_family_tree`. Each has a different purpose:

#### `parse_alleles`
```python
def parse_alleles(bg):
    """
    Checks user input for the correct allele when called in main for each allele, AB, B, A, and O takes input of str bg as input
    """
    # Implementation details...
```

#### `possible_child_blood_types`
```python
def possible_child_blood_types(parent1_bg, parent2_bg, parent1_rh, parent2_rh):
    """
    Calculates possible blood type combinations using:
    - ABO system for allele inheritance
    - Rh system for +/- antigens
    Uses dictionary of tuples/lists for readable syntax.
    """
    # Implementation details...
```

#### `visualize_family_tree`
```python
def visualize_family_tree(child, parent1, parent2):
    """
    Uses Rich library to animate ASCII art visualization.
    Shows inheritance patterns and prints explanation of results.
    """
    # Implementation details...
```

#### `main` Function
- Handles user input, regex capture, and error checking (raising `ValueError`)
- Creates child and person objects for parents and child

#### `Person` Class
```python
class Person:
    """
    Creates child, parent1, and parent2 objects.
    Assigns alleles and Rh antigens to parents for inheritance.
    """
    # Static methods for allele weight assignment and Rh determination

    def __init__(self, parent1=None, parent2=None):
        # Implementation details

    # calling the possible_child_blood_types function to determine Rh and alleles instead of doing it manually in two places
    def assign_blood_type_and_rh(self):
        # Implementation details
```

#### Unit Testing
- Tests for all 3 functions in `test_project.py` (not pushed to github)
- Special consideration given to testing animation functionality

### 2. Installation

1. Download project folder and open in your IDE
2. Navigate to project directory:
   ```bash
   cd project
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python project.py
   ```

#### Alternatively download the executable (.exe) and simply run the Pyinstaller based application.
[BloodGroupTool Installer](https://github.com/Hdave00/ABO-Antigen-Determiner-Tool/releases/tag/v1.0)


### 3. Usage

Follow the terminal prompts and input blood groups in the correct format.

### 4. Sources and Links

- **Genomics Inheritance**: [Veritas](https://www.veritasint.com/blog/en/how-blood-groups-are-inherited-and-why-its-important-that-you-know-yours/) - Founded by George Church (Harvard Medical School)
- **Blood Type Science**: [American Red Cross](https://www.redcrossblood.org/local-homepage/news/article/what-is-a-universal-blood-type-0.html)
- **Research Methodology**: [National Library of Medicine](https://pmc.ncbi.nlm.nih.gov/articles/PMC8873177/)
- **Scientific Literature**: [PubMed](https://pmc.ncbi.nlm.nih.gov/about/disclaimer/)
- **Rich Library**: [Documentation](https://rich.readthedocs.io/en/stable/index.html)