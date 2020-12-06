prepare: #first time only
	pip install pipenv
	pipenv install --dev
monitor: # create cronjob with this. Daily at night
	docker-compose up -d monitor
