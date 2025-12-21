class LocatorsWeb:

    ACCEPT_COOKIES_BUTTON = ".js-message-block__close"

    SEARCH_BUTTON = '[title="Поиск"]'
    INPUT_SEARCH = "#title-search-input"
    SEARCH_RESULT_PRODUCT = 'a.catalog-block__name[href*="molniya-kvark"]'
    NAME_PRODUCT = ".product-detail__name.product-detail__name_mb"

    ADD_TO_CART_BUTTON = (
        ".catalog-block__btn.btn.btn_primary.btn_sm.js-catalog-block__btn"
    )
    CONTINUE_BUYING_BUTTON = ".btn.btn_primary.btn_block.js-modal-close"
    CART_BUTTON = '[id="header_basket_count js-header-cart-click"]'
    SELECT_ALL_PRODUCTS_BUTTON = '[for="cart-select-all"]'
    DELETE_ALL_BUTTON = '[id="cart-delete-all"]'
    EMPTY_CART_TITLE = 'h1[class*="header__title"]'

    CATALOG_BUTTON = '[title="Каталог"]'
    TITLE_CATALOG_SUBWOOFERS = ".page-header__title"
    CATALOG_SUBWOOFERS_BUTTON = (
        'a.nav-submenu__list-link_title[href="/catalog/subwoofers/"]'
    )
    CATALOG_DINAMIKI_BUTTON = (
        'a.nav-submenu__list-link_title[href="/catalog/dinamiki/"]'
    )
    ALL_PRODUCTS_CATALOG = ".catalog-block__name"

    GERMAN_LANGUAGE_BUTTON = '[title = "Немецкий"]'
    ALL_TITLE_NAME_CATALOG = '[class="catalog-tile__name"]'

    LOGIN_PAGE_BUTTON = ".nav-panel__link_login"
    INPUT_USER_LOGIN = '[name="USER_LOGIN"]'
    INPUT_USER_PASSWORD = '[name="USER_PASSWORD"]'
    LOGIN_BUTTON = '[name="Login"]'
    LOGIN_ERROR_MESSAGE = ".auth-error.form-group.form-helper"

    CHECKBOX_SERIES_NAME_AK = '//label[text()="АК"]'
    CHECKBOX_SERIES_NAME_BULAVA = '//label[text()="Булава"]'
    CATALOG_RESULTS_PRODUCTS = '[class="catalog-block__helper"]'
