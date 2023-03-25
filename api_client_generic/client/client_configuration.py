""" Client configuration class """
import os
import yaml
import json
from api_client_generic.const import ROOT_DIR


class ClientCfg:
    """ configuration class for the API client """
    def __init__(self):
        pass


    def __check_for_cfg(self, path: str) -> bool:
        """
        Check for a configuration file.

        :type: None
        :rtype: bool
        :returns: True if configuration was found
        :raises FileNotFoundError: if file was not found
        :raises IncorrectFiletypeError: If the file was not the correct type

        """
        if not isinstance(path, str):
            raise TypeError(f'path should have been a str but got a: {type(path)}')
        if os.path.isfile(path) is True:
            return True
        else:
            raise FileNotFoundError(f'the path: {path} did not resolve. Check path')


    def __evaluate_ssl_certificate(self, cert_path: str) -> bool:
        """
        Evaulate a certificate file. Valid filetypes are defined in the
        api_client_generic/configuration/config.yaml

        :type cert_path: str
        :param cert_path: the path of the certificate file to use
        :rtype: bool
        :returns: True if the certificate is good
        :raises IncorrectFiletypeError: if the cert is in an not a good type
        :raises TypeError: if cert_path is not a string
        :raises FileNotFoundError: if the certificate path doesnt resolve

        """
        if not isinstance(cert_path, str):
            raise TypeError(f'cert_path should have been a str but got a: {type(cert_path)}')
        if os.path.isfile(os.path.isfile(cert_path)) is False:
            raise FileNotFoundError(f'path: {cert_path} did not resolve. Check your config.')
        filetype = cert_path.split('.')[-1]
        if filetype not in libconf.cert_types:
            raise IncorrectFileTypeError(f'filetype: {filetype} is not in {libconf.cert_types}')
        return True


    def __load_configuration(self, path: str) -> dict:
        """
        Load the specified configuration into the class.

        :type path: str
        :param path: the path to the configuration
        :rtype: dict
        :returns: a dictionary of the configuration
        :raises TypeError: if path is not a str

        """
        if not isinstance(path, str):
            raise TypeError(f'path should have been a str but got a: {type(path)}')
        with open(path, 'r', encoding='utf-8') as file:
            config = json.load(fp=file)
        return config




class IncorrectFileTypeError(Exception):
    """ Exception type for invalid filetypes """
    pass



