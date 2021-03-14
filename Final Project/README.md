# Description

A double pendulum simulator with dynamics & chaos analyzer (written in Python 3) which uses the [fourth order Runge-Kutta
(RK4) method](https://lpsa.swarthmore.edu/NumInt/NumIntFourth.html) to solve the set of differential equations from either the
[Lagrangian formulation](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Statistical_Mechanics/Advanced_Statistical_Mechanics/Classical_microstates%2C_Newtonian%2C_Lagrangian_and_Hamiltonian_mechanics/The_Lagrangian_formulation_of_classical_mechanics#:~:text=For%20conservative%20systems%2C%20there%20is,function%20of%20positions%20and%20velocities.https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Statistical_Mechanics/Advanced_Statistical_Mechanics/Classical_microstates%2C_Newtonian%2C_Lagrangian_and_Hamiltonian_mechanics/The_Lagrangian_formulation_of_classical_mechanics#:~:text=For%20conservative%20systems%2C%20there%20is,function%20of%20positions%20and%20velocities.)
or from the [Hamiltonian formulation](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Statistical_Mechanics/Advanced_Statistical_Mechanics/Classical_microstates%2C_Newtonian%2C_Lagrangian_and_Hamiltonian_mechanics/The_Hamiltonian_formulation_of_classical_mechanics#:~:text=The%20Hamiltonian%20of%20a%20system,What%20are%20conjugate%20momenta%3F&text=The%20solution%20of%20Hamilton's%20equations,momenta%20as%20functions%20of%20time.)
for the double pendulum system.

# Required modules

The following modules are used:

- [Pickle](https://docs.python.org/3/library/pickle.html) {Default module. NO NEED TO INSTALL}
- [Matplotlib](https://matplotlib.org/stable/index.html)
- [Pygame](https://www.pygame.org/news)
- [Math](https://docs.python.org/3/library/math.html) {Default module. NO NEED TO INSTALL}
- [Analysis](https://pypi.org/project/analysis/)
- [NumPy](https://numpy.org/)

For installing **Matplotlib**, the commands are the following:

    python -m pip install -U pip
    python -m pip install -U matplotlib

For installing **Pygame**, the command is the following:

    python3 -m pip install -U pygame --user

For installing **Analysis**, the command is the following:

    pip install analysis

For installing **NumPy**, the command is the following:

    pip install numpy


# Usage instructions

Run `double-pendulum.py` to get the simulation and the simulation parameters which can
be hard coded manually. After quitting simulation, all the graphs will be available consequently. 


# Contributors & contact information

- S.M. Raihanul Bashir / raihanulbashirhridoy@gmail.com
- Ahmad Al - Imtiaz / ahmadal.imtiaz@gmail.com
- Md Tahsin Ahammad / tashinahammad.03@gmail.com
- Md Kawser Ahmed / kawserahmedseyam13@gmail.com
- Tanver Hossain Refat / tanveerrefat2223@gmail.com
