"""
Parent class for the engine.
"""


class Engine:
    """
    Parent class for an engine.

    An engine is an object that can generate data for the environment. Currently we
    have only an espresso model but this should be kept generic to allow for an
    experimental interface.
    """

    def setup_simulation(self) -> None:
        """
        optional: prepare the simulation before integration
        """
        pass

    def integrate(self, n_slices: int, force_model) -> None:
        """

        Parameters
        ----------
        n_slices: int
            Number of time slices to integrate
        force_model
            A an object that has to have a ``calc_force`` method
        """
        raise NotImplementedError("Implemented in child class.")

    def get_particle_data(self) -> dict:
        """
        Get position, velocity and director of the particles as a dict of np.array
        """
