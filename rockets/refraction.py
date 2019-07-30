import numpy as np

def snell(theta_in,n1,n2):
    """
    Here is some documentation: remember Snell's law from UG? Thought not.
    
    Compute the refraction angle using Snell's Law: Sin(theta_1)/Sin(theta_2)=n1/n2.
    
    See https://numpydoc.readthedocs.io/en/latest/format.html for format guide
    
    Parameters
    ----------
    theta_inc: float
        Incident angle in Radians
        
    n1, n2: float
        The refractive index of the original medium (n1) and exit medium (n2)
        
    Returns
    -------
    theta_out: float
        The refraction angle
        
    Example:
    ------
    snell(np.pi/4,1.00,1.33)
    0.5605584137424605
    """
    
    return np.arcsin((n1/n2)*np.sin(theta_in))