from typing import Generator

import pandas as pd


class StudentsRepository:
    def __init__(
        self,
        df: pd.DataFrame,
        identifications_fields: list[str],
    ):
        self._df = df
        self._identifications_fields = identifications_fields

    def get_df(self) -> pd.DataFrame:
        return self._df

    def get_list(self) -> Generator[tuple[list, int], None, None]:
        for index, row in self._df.iterrows():
            yield row[self._identifications_fields].tolist(), index

    def find_by_substring(self, substring: str) -> Generator[tuple[list, int], None, None]:
        substring = substring.lower()
        mask = self._df[self._identifications_fields].apply(
            lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1
        )
        for index in self._df[mask].index:
            yield self._df.loc[index, self._identifications_fields].tolist(), index
