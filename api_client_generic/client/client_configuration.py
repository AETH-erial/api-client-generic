""" Client configuration class """
import os
import yaml
import json
import toml
from enum import Enum
from api_client_generic.const import ROOT_DIR
from api_client_generic.configuration.library_controller import LibraryController




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
        cert_types = LibraryController().ssl_cert_types()
        if not isinstance(cert_path, str):
            raise TypeError(f'cert_path should have been a str but got a: {type(cert_path)}')
        if os.path.isfile(os.path.isfile(cert_path)) is False:
            raise FileNotFoundError(f'path: {cert_path} did not resolve. Check your config.')
        filetype = cert_path.split('.')[-1]
        if filetype not in cert_types:
            raise IncorrectFileTypeError(f'filetype: {filetype} is not in {cert_types}')
        return True


    def __validate_config_fields(self, config: dict) -> bool:
        """
        Validate the config fields provided in the configuration

        :type config: dict
        :param config: the configuration to be validated
        :rtype: bool
        :returns: True if the fields check out
        :raises IndexError: if incorrect number of fields are present
        :raises TypeError: if config is not a dict
        :raises KeyError: if an incorrect fieldname is passed

        """
        if not isinstance(config, dict):
            raise TypeError(f'config should have been a dictionary but recieved a: {type(config)}')
        approved_fieldnames = LibraryController().client_config_fieldnames
        if len(config.keys()) != len(approved_fieldnames):
            raise IndexError(
                f'{len(cohfig.keys())} was passed. Only: {len(client_config_fieldnames)} allowed')
        for field in config.keys():
            if field not in approved_fieldnames:
                raise ValueError(
                    f'{field} not in approved fieldnames: {approved_fieldnames}')
        return True


    def __evaluate_client_configuration(self, config_path: str) -> ConfigurationTypes:
        """
        Evaluate the passed configuration type and parse it based on the extension
        
        :type config_path: str
        :param config_path: the path to the configuration
        :rtype: ConfigurationTypes
        :param ConfigurationTypes: Enum class holding the approved config types
        :returns: an enum instance with the config filetype
        :raises IncorrectFileTypeError: if the passed config is not an approved type
        :raises FileNotFoundError: if the file cant be found

        """
        if os.path.isfile(config_path) is False:
            raise FileNotFoundError(f'File: {config_path} not found. Check path.')
        filetype = config_path.split('.')[-1]
        if filetype in ConfigurationTypes.values():
            return getattr(ConfigurationTypes, filetype)
        raise IncorrectFileTypeError(f'Passed config: {config_path} not in an approved format: {ConfigurationTypes.values()}')


    def __load_conf_from_json(self, path: str) -> dict:
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

    def __load_conf_from_yaml(self, path: str) -> dict:
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
            config = yaml.load(file)
        return config  


    def __load_conf_from_toml(self, path: str) -> dict:
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
            config = toml.load(file)
        return config  


class ConfigurationTypes(Enum):
    """ filetypes to be used as client configuration files. """
    JSON = 'json'
    YAML = 'yaml'
    TOML = 'toml'

    @classmethod
    def values(cls) -> list:
        """
        Returns a list of the enums values
        """
        return_list = []
        for value in cls._member_names_: # pylint: disable=no-member
            return_list.append(getattr(cls, value).value)
        return return_list



class IncorrectFileTypeError(Exception):
    """ Exception type for invalid filetypes """
    pass















