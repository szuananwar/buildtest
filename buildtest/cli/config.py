import getpass
import json
import os
import shutil
import sys

import yaml
from buildtest import BUILDTEST_VERSION
from buildtest.defaults import BUILDSPEC_CACHE_FILE, console, supported_schemas
from buildtest.exceptions import ConfigurationError
from buildtest.executors.setup import BuildExecutor
from buildtest.system import system
from buildtest.utils.file import read_file
from jsonschema import ValidationError
from tabulate import tabulate
from termcolor import colored


def config_cmd(args, configuration):
    """Entry point for ``buildtest config`` command. This method will invoke other methods depending on input argument.

    Args:
        args (dict): Parsed arguments from `ArgumentParser.parse_args <https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.parse_args>`_
        configuration (buildtest.config.SiteConfiguration): An instance of SiteConfiguration class
    """
    if args.config == "view":
        view_configuration(configuration)

    elif args.config == "executors":
        buildexecutor = BuildExecutor(configuration)
        view_executors(
            configuration,
            buildexecutor,
            args.json,
            args.yaml,
            args.disabled,
            args.invalid,
        )

    elif args.config == "summary":
        view_summary(configuration)

    elif args.config == "validate":
        validate_config(configuration)

    elif args.config == "systems":
        view_system(configuration)


def view_system(configuration):
    """This method implements command ``buildtest config systems`` which displays
    system details from configuration file in table format.

    Args:
        configuration (buildtest.config.SiteConfiguration): An instance of SiteConfiguration class
    """

    table = {"system": [], "description": [], "hostnames": [], "moduletool": []}
    for name in configuration.config["system"].keys():
        table["system"].append(name)
        table["description"].append(
            configuration.config["system"][name].get("description")
        )
        table["moduletool"].append(configuration.config["system"][name]["moduletool"])
        table["hostnames"].append(configuration.config["system"][name]["hostnames"])

    if os.getenv("BUILDTEST_COLOR") == "True":
        print(
            tabulate(
                table,
                headers=[
                    colored(field, "blue", attrs=["bold"]) for field in table.keys()
                ],
                tablefmt="grid",
            )
        )
        return

    print(tabulate(table, headers=table.keys(), tablefmt="grid"))


def validate_config(configuration):
    """This method implements ``buildtest config validate`` which attempts to
    validate buildtest schema file `settings.schema.json <https://github.com/buildtesters/buildtest/blob/devel/buildtest/schemas/settings.schema.json>`_.
    If it's not validate an exception is raised which could be
    `jsonschema.exceptions.ValidationError <https://python-jsonschema.readthedocs.io/en/stable/errors/#jsonschema.exceptions.ValidationError>`_
    or :class:`buildtest.exceptions.ConfigurationError`.

    If configuration is valid buildtest print something as follows.

    .. code-block:: console

        bash-3.2$ buildtest config validate
        /Users/siddiq90/Documents/GitHubDesktop/buildtest/buildtest/settings/config.yml is valid


    If there is an error validating configuration file, buildtest will print error message reported by exception

    Args:
        configuration (buildtest.config.SiteConfiguration): An instance of SiteConfiguration class

    Raises:
        SystemExit: If exception is raised during validating configuration file.
    """

    try:
        configuration.validate()
    except (ValidationError, ConfigurationError) as err:
        print(err)
        raise sys.exit(f"{configuration.file} is not valid")

    print(f"{configuration.file} is valid")


def view_configuration(configuration):
    """Display content of buildtest configuration file. This implements command ``buildtest config view``"""

    console.rule(configuration.file)
    console.print(read_file(configuration.file))


def view_executors(
    configuration,
    buildexecutor,
    json_format=False,
    yaml_format=False,
    disabled=False,
    invalid=False,
):
    """Display executors from buildtest configuration. This implements ``buildtest config executors`` command.

    Args:
        configuration (buildtest.config.SiteConfiguration): An instance of SiteConfiguration class
        buildexecutor (buildtest.executors.setup.BuildExecutor): An instance of BuildExecutor class
        json_format (bool): Display output in json format which is specified via ``buildtest config executors --json``
        yaml_format (bool): Display output in yaml format which is specified via ``buildtest config executors --yaml``
        disabled (bool): Display list of disabled executors which is specified via ``buildtest config executors --disabled``
        invalid (bool): Display list of invalid executors which is specified via ``buildtest config executors --invalid``
    """

    d = {"executors": configuration.target_config["executors"]}

    # display output in JSON format
    if json_format:
        print(json.dumps(d, indent=2))
        return

    # display output in YAML format
    if yaml_format:
        print(yaml.dump(d, default_flow_style=False))
        return

    if disabled:
        executors = configuration.disabled_executors
        if not executors:
            print("There are no disabled executors")
            return

        for executor in executors:
            print(executor)
        return

    if invalid:
        executors = configuration.invalid_executors
        if not executors:
            print("There are no invalid executors")
            return

        for executor in executors:
            print(executor)
        return

    names = buildexecutor.list_executors()
    for name in names:
        print(name)


def view_summary(configuration, buildtestsystem=None):
    """This method implements ``buildtest config summary`` option. In this method
    we will display a summary of System Details, Buildtest settings, Schemas,
    Repository details, Buildspecs files and test names.

    Args:
        configuration (buildtest.config.SiteConfiguration): An instance of SiteConfiguration class
        buildexecutor (buildtest.executors.setup.BuildExecutor): An instance of BuildExecutor class
    """

    system_details = buildtestsystem or system

    print("buildtest version: ", BUILDTEST_VERSION)
    print("buildtest Path:", shutil.which("buildtest"))

    print("\n")
    print("Machine Details")
    print("{:_<30}".format(""))
    print("Operating System: ", system_details.system["os"])
    print("Hostname: ", system_details.system["host"])
    print("Machine: ", system_details.system["machine"])
    print("Processor: ", system_details.system["processor"])
    print("Python Path", system_details.system["python"])
    print("Python Version:", system_details.system["pyver"])
    print("User:", getpass.getuser())

    print("\n")

    print("Buildtest Settings")
    print("{:_<80}".format(""))
    print(f"Buildtest Settings: {configuration.file}")

    executors = []
    for executor_type in configuration.target_config.get("executors").keys():
        for name in configuration.target_config["executors"][executor_type].keys():
            executors.append(f"{executor_type}.{name}")

    print("Executors: ", executors)

    print("Buildspec Cache File:", BUILDSPEC_CACHE_FILE)
    print("\n")

    print("Buildtest Schemas")
    print("{:_<80}".format(""))
    print("Available Schemas:", supported_schemas)
