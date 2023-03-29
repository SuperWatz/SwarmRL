"""
Module implementing different loss models.
"""
from swarmrl.losses.policy_gradient_loss import PolicyGradientLoss
from swarmrl.losses.proximal_policy_loss import ProximalPolicyLoss
from swarmrl.losses.proximal_policy_loss_shared import SharedProximalPolicyLoss

__all__ = [
    PolicyGradientLoss.__name__,
    ProximalPolicyLoss.__name__,
    SharedProximalPolicyLoss.__name__,
]
