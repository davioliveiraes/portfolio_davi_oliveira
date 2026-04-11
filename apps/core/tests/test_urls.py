from django.urls import resolve, reverse


class TestURLs:
    """Testa se as URLs resolvem para as views corretas."""

    def test_home_url(self):
        assert resolve(reverse("core:home")).view_name == "core:home"

    def test_sobre_url(self):
        assert resolve("/sobre/").view_name == "core:sobre"

    def test_competencias_url(self):
        assert resolve("/competencias/").view_name == "core:competencias"

    def test_projetos_url(self):
        assert resolve("/projetos/").view_name == "core:projetos"

    def test_experiencias_url(self):
        assert resolve("/experiencias/").view_name == "core:experiencias"

    def test_formacao_url(self):
        assert resolve("/formacao/").view_name == "core:formacao"

    def test_contato_url(self):
        assert resolve("/contato/").view_name == "core:contato"

    def test_app_namespace(self):
        assert resolve("/").app_name == "core"
