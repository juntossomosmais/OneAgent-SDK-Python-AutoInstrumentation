from django.apps import AppConfig, apps
from ...log import logger
from .wrapper import instrument_django


class DynatraceConfig(AppConfig):
    name = "autodynatrace.wrappers.django"
    label = "dynatrace_django"

    def ready(self):
        import oneagent
        sdk_options = oneagent.sdkopts_from_commandline(remove=True)
        is_forkable_enabled = bool(strtobool(os.getenv("AUTODYNATRACE_FORKABLE", "True")))
        oneagent.initialize(sdk_options, forkable=is_forkable_enabled)
        instrument_django()
