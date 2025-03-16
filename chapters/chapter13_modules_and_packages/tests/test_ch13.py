import pytest

# from PyTime.date_conversion import is_leap_year
# from PyTime.time_conversion import hours_to_minutes, minutes_to_seconds, seconds_to_minutes


@pytest.mark.skip(reason="No implementation")
def test_e93():
    raise NotImplementedError(
        """TODO:
                Write tests by importing PyTime package.
                from PyTime.date_conversion import is_leap_year
                - is_leap_year(2024) is True
                - is_leap_year(2025) is False

                from PyTime.time_conversion import hours_to_minutes, minutes_to_seconds, seconds_to_minutes
                - hours_to_minutes(1) == 60
                - minutes_to_seconds(1) == 60
                - seconds_to_minutes(60) == 1
                """
    )
