""" Class for the Library Controller class """
import yaml
import os
from api_client_generic.const import ROOT_DIR



class LibraryController:
    """
    Controller class that reads and returns global configuration settings and values
    """
    def __init__(self) -> None:
        pass


    def client_config_fieldnames(self) -> list:
        """
        Return a list of the fieldnames specified in the libconf.yml file

        :param: None
        :rtype: list
        :returns: a list of the fieldnames
        :raises: None

        """
        pass


    def ssl_cert_types(self) -> list:
        """
        Returns a list of set SSL file extension types in the libconf.yml file
        
        :param: None
        :rtype: list
        :returns: a list of the file extensions
        :raises None
        
        """
        pass


