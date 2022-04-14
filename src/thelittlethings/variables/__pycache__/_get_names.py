import inspect


def get_names(var):
    back_frame = inspect.currentframe().f_back
    callers_local_vars = list(back_frame.f_locals.items())
    callers_global_vars = list(back_frame.f_globals.items())
    callers_vars = callers_local_vars + [var for var in callers_global_vars if var not in callers_local_vars]
    return [var_name for var_name, var_val in callers_vars if var_val is var]