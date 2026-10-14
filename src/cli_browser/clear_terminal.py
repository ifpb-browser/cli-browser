ANSI_CLEAR_TERMINAL_ESCAPE_CODE = "\033c"


def clear_terminal() -> None:
    print(ANSI_CLEAR_TERMINAL_ESCAPE_CODE, end="")
