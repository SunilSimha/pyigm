""" Simple Class for a Galaxy
  Likely to be replaced with an external Class
"""

from __future__ import print_function, absolute_import, division, unicode_literals

import pdb

from astropy import units as u

from linetools.utils import radec_to_coord
from linetools import utils as ltu

class Galaxy(object):
    """A Galaxy Class

    Parameters
    ----------
    radec : tuple or SkyCoord
      (RA,DEC) in deg or astropy.coordinate
    z : float, optional
      Redshift

    Attributes
    ----------
    name : str
        Name(s)
    z : float, optional
       Adopted redshift
    coord : SkyCoord
    """
    # Initialize with a .dat file
    def __init__(self, radec, z=None):
        self.coord = radec_to_coord(radec)
        # Redshift
        self.z = z
        
        # Name
        self.name = ('J'+self.coord.ra.to_string(unit=u.hour, sep='', pad=True)+
                    self.coord.dec.to_string(sep='', pad=True, alwayssign=True))

    def to_dict(self):
        """ Convert the galaxy to a JSON-ready dict for output

        Returns
        -------
        gdict : dict

        """
        import datetime
        import getpass
        date = str(datetime.date.today().strftime('%Y-%b-%d'))
        user = getpass.getuser()
        # Generate the dict
        gdict = dict(Name=self.name,
                       RA=self.coord.ra.value,
                       DEC=self.coord.dec.value,
                       CreationDate=date,
                       user=user
                       )
        if self.z is not None:
            gdict['z'] = self.z
        # Polish
        gdict = ltu.jsonify(gdict)
        # Return
        return gdict

    # #############
    def __repr__(self):
        return ('<Galaxy: {:s} {:s} {:s}, z={:g}>'.format(
                 self.name, 
                 self.coord.ra.to_string(unit=u.hour, sep=':', pad=True),
                 self.coord.dec.to_string(sep=':', pad=True, alwayssign=True),
                 self.z))



