"""
"""
from landlab.components import ChiFinder


def _validate_chi_finder(chi_finder):
    if not isinstance(chi_finder, ChiFinder):
        msg = ""
        raise ValueError(msg)


def chi_intercept(chi_finder):
    r"""Return the intercept to a linear fit through a :math:`\Chi`-z plot.

    This is a loose wrapper around the function
    `ChiFinder.best_fit_chi_elevation_gradient_and_intercept`.

    Parameters
    ----------
    chi_finder : an instance of a `ChiFinder`

    Returns
    -------
    out : float
        The intercept value.

    Examples
    --------
    First an example that only uses the ``chi_intercept`` function.

    >>> import numpy as np
    >>> from landlab import RasterModelGrid
    >>> from landlab.components import FlowAccumulator, ChiFinder
    >>> from umami.calculations import chi_intercept
    >>> grid = RasterModelGrid((10, 10))
    >>> z = grid.add_zeros("node", "topographic__elevation")
    >>> z += grid.x_of_node**2 + grid.y_of_node**2
    >>> fa = FlowAccumulator(grid)
    >>> fa.run_one_step()
    >>> cf = ChiFinder(grid, min_drainage_area=1.0)
    >>> cf.calculate_chi()
    >>> np.round(chi_intercept(cf), decimals=0)
    -4.0

    Next, the same calculations are shown as part of an umami ``Metric``.

    >>> from io import StringIO
    >>> from umami import Metric
    >>> grid = RasterModelGrid((10, 10))
    >>> z = grid.add_zeros("node", "topographic__elevation")
    >>> z += grid.x_of_node**2 + grid.y_of_node**2
    >>> file_like=StringIO('''
    ... ci:
    ...     _func: chi_intercept
    ... ''')
    >>> metric = Metric(grid, chi_finder_kwds={"min_drainage_area": 1.0})
    >>> metric.add_metrics_from_file(file_like)
    >>> metric.names
    odict_keys(['ci'])
    >>> metric.calculate_metrics()
    >>> np.round(metric.values, decimals=0)
    array([-4.])
    """
    _validate_chi_finder(chi_finder)
    slp, incp = chi_finder.best_fit_chi_elevation_gradient_and_intercept()
    return incp


def chi_gradient(chi_finder):
    r"""Return the slope to a linear fit through a :math:`\Chi`-z plot.

    This is a loose wrapper around the function
    `ChiFinder.best_fit_chi_elevation_gradient_and_intercept`.

    Parameters
    ----------
    chi_finder : an instance of a `ChiFinder`

    Returns
    -------
    out : float
        The slope value.

    Examples
    --------
    First an example that only uses the ``chi_gradient`` function.

    >>> import numpy as np
    >>> from landlab import RasterModelGrid
    >>> from landlab.components import FlowAccumulator, ChiFinder
    >>> from umami.calculations import chi_intercept
    >>> grid = RasterModelGrid((10, 10))
    >>> z = grid.add_zeros("node", "topographic__elevation")
    >>> z += grid.x_of_node**2 + grid.y_of_node**2
    >>> fa = FlowAccumulator(grid)
    >>> fa.run_one_step()
    >>> cf = ChiFinder(grid, min_drainage_area=1.0)
    >>> cf.calculate_chi()
    >>> np.round(chi_gradient(cf), decimals=0)
    23.0

    Next, the same calculations are shown as part of an umami ``Metric``.

    >>> from io import StringIO
    >>> from umami import Metric
    >>> grid = RasterModelGrid((10, 10))
    >>> z = grid.add_zeros("node", "topographic__elevation")
    >>> z += grid.x_of_node**2 + grid.y_of_node**2
    >>> file_like=StringIO('''
    ... cg:
    ...     _func: chi_gradient
    ... ''')
    >>> metric = Metric(grid, chi_finder_kwds={"min_drainage_area": 1.0})
    >>> metric.add_metrics_from_file(file_like)
    >>> metric.names
    odict_keys(['cg'])
    >>> metric.calculate_metrics()
    >>> np.round(metric.values, decimals=0)
    array([ 23.])
    """
    _validate_chi_finder(chi_finder)
    slp, incp = chi_finder.best_fit_chi_elevation_gradient_and_intercept()
    return slp
