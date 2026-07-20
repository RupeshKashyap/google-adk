adk deploy cloud_run \
--project=rupesh-dev-55895 \
--region=us-central1 \
--service_name=adk-demo \
--app_name=content_creation_agent \
--with_ui \
./content_creation_agent


# Session Creation
curl -X POST "https://adk-demo-1085445996177.us-central1.run.app/apps/content_creation_agent/users/vish/sessions" \
  -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json" \
  -d '{}'

#output
  {"id":"e3738ac3-00e2-4155-9510-252134c5fd9c","appName":"content_creation_agent","userId":"vish","state":{},"events":[],"lastUpdateTime":1775592267.0042644}

  #Query
curl -N -X POST "https://adk-demo-1085445996177.us-central1.run.app/run_sse" \
  -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json" \
  -d '{
        "app_name": "content_creation_agent",
        "user_id": "vish",
        "session_id": "e3738ac3-00e2-4155-9510-252134c5fd9c",
        "newMessage": {
          "role": "user",
          "parts": [{ "text": "Create content on RAG" }]
        }
      }'