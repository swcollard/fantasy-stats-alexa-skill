# /bin/sh

##
# Build script for project. Cleans, generates, and uploads build artifacts to AWS Lambda.
##

rm fantasy_skill.zip
zip -r fantasy_skill.zip *.py
aws lambda update-function-code --function-name FantasyFootballStatsSkill --zip-file fileb://fantasy_skill.zip
