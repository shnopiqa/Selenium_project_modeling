import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:

    def test_button_add_to_basket_is_visible(self, language):
        """Тест проверяет, что страница товара
         содержит кнопку добавления в корзину
        """
        # Открываем страницу товара
        language.get(link)

        # Установлено время принудительной задержки браузера
        # после открытия страницы, для визуальной проверки языка открытой страницы
        time.sleep(5)

        # Проверяем наличие кнопки добавления товара в корзину
        assert language.find_element_by_css_selector("button.btn-add-to-basket")