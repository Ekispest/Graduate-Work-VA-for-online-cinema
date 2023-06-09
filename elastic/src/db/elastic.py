from typing import Any

from db.storage import AbstractStorage


class StorageElasticsearch(AbstractStorage):
    async def get(self, index: str, target_id: str) -> Any:
        return await self.storage.get(index=index, id=target_id)

    async def search(self, index: str, _source, body, sort) -> Any:
        return await self.storage.search(index=index, _source=_source, body=body, sort=sort)

    async def close(self) -> None:
        await self.storage.close()
