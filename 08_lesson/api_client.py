class YougileAPIClient:
    def __init__(self, use_mock=False):
        self.use_mock = use_mock
              
    def create_project(self, title, description=None):
        if not title or not isinstance(title, str) or not title.strip():
            raise ValueError("Invalid title")
        if self.use_mock:
            mock_response = MagicMock()
            mock_response.status_code = 201
            mock_response.json.return_value = {
                "id": "mock_prj_123",
                "title": title,
                "description": description
            }
            return mock_response
  
    def get_project(self, project_id):
        if self.use_mock:
            mock_response = MagicMock()
            if project_id == "invalid_id_999":
                mock_response.status_code = 404
                mock_response.json.return_value = {"error": "Project not found"}
            else:
                mock_response.status_code = 200
                mock_response.json.return_value = {
                    "id": project_id,
                    "title": "Mock Project"
                }
            return mock_response


    def update_project(self, project_id, **kwargs):
        if not kwargs:
            raise ValueError("No fields to update")
        if self.use_mock:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                "id": project_id,
                **kwargs
            }
            return mock_response