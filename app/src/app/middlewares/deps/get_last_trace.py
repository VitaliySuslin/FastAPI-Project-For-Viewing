import traceback


async def get_last_trace():
    try:
        trace_ = traceback.format_exc()
        return str(trace_)[-200:].split("\n")
    except Exception:
        pass