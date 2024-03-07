import re
import types


def humanify(name: str):
    return ' '.join(re.split('_+', name))


def step(fn):
    def fn_with_logging(*args, **kwargs):
        fn_name = humanify(fn.__name__)
        is_method = (
            args
            and isinstance(args[0], object)
            and isinstance(getattr(args[0], fn.__name__), types.MethodType)
        )
        args_to_log = args[1:] if is_method else args
        args_kwargs_to_log_as_string = [
            *(map(str, args_to_log)),
            *[f'{key}={value}' for key, value in kwargs.items()],
        ]
        print(
            (f'[{args[0].__class__.__name__}] ' if is_method else '')
            + fn_name
            + (
                ': ' + ','.join(map(str, args_kwargs_to_log_as_string))
                if args_kwargs_to_log_as_string
                else ''
            )
        )
        return fn(*args, **kwargs)

    return fn_with_logging


class SignUpForm:
    @step
    def fill_first_name(self, *args, **kwargs):
        ...

    @step
    def fill_email(self, value):
        ...

    @step
    def fill_password(self, value):
        ...

    @step
    def submit(self):
        ...


sign_up_form = SignUpForm()


class DashBoard:
    @step
    def get_user_info(self):
        ...


profile = DashBoard()


@step
def given_sign_up_form_opened():
    ...


given_sign_up_form_opened()
sign_up_form.fill_first_name('cdcd', 'xsxsxs', 'ARGS', value='Vladimir', lastname='1111Vladimir')
sign_up_form.fill_email('dwehnchb@mail.ru')
sign_up_form.fill_password('qazw')
sign_up_form.submit()
profile.get_user_info()
