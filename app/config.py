from environs import Env

class Settings:
	env = Env()
	env.read_env()

	DB_USER=env("DB_USER")
	DB_PASS=env('DB_PASS')
	DB_HOST=env('DB_HOST')
	DB_PORT=env('DB_PORT')
	DB_NAME=env('DB_NAME')

	SECRET_KEY = env('SECRET_KEY')
	ALGORITHM = env('ALGORITHM')

	SMTP_USER=env('SMTP_USER')
	SMTP_PASS=env('SMTP_PASS')
	SMTP_HOST=env('SMTP_HOST')
	SMTP_PORT=env('SMTP_PORT')


settings = Settings()