"""
Module for a classical protocol.
"""
from swarmrl.observables.observable import Observable
from swarmrl.rl_protocols.rl_protocol import RLProtocol
from swarmrl.tasks.task import Task


class ClassicalAlgorithm(RLProtocol):
    """
    Class to handle the classical algortihms.
    """

    def __init__(
        self,
        particle_type: int,
        policy: callable,
        observable: Observable,
        task: Task,
        actions: dict,
    ):
        """
        Constructor for the actor-critic protocol.

        Parameters
        ----------
        policy : callable
                Policy to use for the protocol.
        task : Task
                A metric for the classical algorithm.
        particle_type : int
                Particle ID this RL protocol applies to.
        observable : Observable
                Observable for this particle type
        actions : dict
                Actions allowed for the particle.
        """
        self.particle_type = particle_type
        self.policy = policy
        self.task = task
        self.observable = observable
        self.actions = actions

    def compute_episode_step(self,
                             item,
                             colloids,
                             actions,
    ):

        observables_computed = self.observable.compute_observable(colloids)
        rewards = self.task(colloids)
        chosen_actions = self.policy.compute_action(
            observables=observables_computed, explore_mode=False)

        count = 0  # Count the colloids of a specific species.
        for colloid in colloids:
            if str(colloid.type) == item:
                actions[colloid.id] = chosen_actions[count]
                count += 1

        trajectory_data = {"obs": observables_computed,
                           "action_indices": None,
                           "log_probs": None,
                           "rewards": rewards}
        return observables_computed, rewards, actions, trajectory_data