# Description

A double pendulum simulator with dynamics & chaos analyzer (written in Python 3) which uses the [fourth order Runge-Kutta
(RK4) method](https://lpsa.swarthmore.edu/NumInt/NumIntFourth.html) to solve the set of differential equations from either the
[Lagrangian formulation](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Statistical_Mechanics/Advanced_Statistical_Mechanics/Classical_microstates%2C_Newtonian%2C_Lagrangian_and_Hamiltonian_mechanics/The_Lagrangian_formulation_of_classical_mechanics#:~:text=For%20conservative%20systems%2C%20there%20is,function%20of%20positions%20and%20velocities.https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Statistical_Mechanics/Advanced_Statistical_Mechanics/Classical_microstates%2C_Newtonian%2C_Lagrangian_and_Hamiltonian_mechanics/The_Lagrangian_formulation_of_classical_mechanics#:~:text=For%20conservative%20systems%2C%20there%20is,function%20of%20positions%20and%20velocities.)
or from the [Hamiltonian formulation](https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Statistical_Mechanics/Advanced_Statistical_Mechanics/Classical_microstates%2C_Newtonian%2C_Lagrangian_and_Hamiltonian_mechanics/The_Hamiltonian_formulation_of_classical_mechanics#:~:text=The%20Hamiltonian%20of%20a%20system,What%20are%20conjugate%20momenta%3F&text=The%20solution%20of%20Hamilton's%20equations,momenta%20as%20functions%20of%20time.)
for the double pendulum system.

# Required modules

The following modules are used:

- `numpy`
- `pygame`

You can install them with the following command:

    pip3 install pygame numpy

# Usage instructions

Run `double-pendulum.py` to get the simulation and the simulation parameters which can
be set.

# Notes on stability

If your simulation becomes unstable, try doing one or more of the following:

- reduce the time step
- reduce the initial angular velocities
- reduce the gravitational acceleration

# Contributors & contact information

- S.M. Raihanul Bashir / raihanulbashirhridoy@gmail.com
- 
