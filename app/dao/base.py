from sqlalchemy import insert, select
from app.database import async_session_maker

class BaseDAO:
	model = None


	@classmethod
	async def find_by_id(cls, model_id):
		async with async_session_maker() as session:
					query = select(cls.model).filter_by(id=model_id)
					result = await session.execute(query)
					return result.scalar_one_or_none()


	@classmethod
	async def find_one_or_none(cls, **folter_by):
		async with async_session_maker() as session:
					query = select(cls.model).filter_by(**folter_by)
					result = await session.execute(query)
					return result.scalar_one_or_none()


	@classmethod
	async def find_all(cls, **folter_by):
		async with async_session_maker() as session:
			query = select(cls.model).filter_by(**folter_by)
			result = await session.execute(query)
			# return result.mappings().all()
			return result.scalars().all()


	@classmethod
	async def add(cls, **data):
		async with async_session_maker() as session:
			query = insert(cls.model).values(**data)
			await session.execute(query)
			await session.commit()