"""Unit tests cho MenuService (Issue #1)."""

import pytest
from src.menu_service import MenuItem, MenuService


@pytest.fixture
def service() -> MenuService:
    svc = MenuService()
    svc.add_item(MenuItem(item_id="M01", name="Cơm chiên Dương Châu", price=35000.0, category="Cơm chiên"))
    svc.add_item(MenuItem(item_id="M02", name="Cơm chiên hải sản", price=40000.0, category="Cơm chiên"))
    svc.add_item(MenuItem(item_id="D01", name="Trà đá", price=5000.0, category="Đồ uống"))
    return svc


def test_add_item_success():
    svc = MenuService()
    item = svc.add_item(MenuItem(item_id="M01", name="Cơm chiên gà", price=35000.0, category="Cơm chiên"))
    assert item.item_id == "M01"
    assert svc.get_item("M01") is not None


def test_add_item_duplicate_id_raises(service: MenuService):
    with pytest.raises(ValueError, match="đã tồn tại"):
        service.add_item(MenuItem(item_id="M01", name="Trùng mã", price=30000.0, category="Cơm chiên"))


def test_add_item_invalid_price_raises():
    svc = MenuService()
    with pytest.raises(ValueError, match="Đơn giá không thể là số âm"):
        svc.add_item(MenuItem(item_id="M01", name="Cơm chiên", price=-1000.0, category="Cơm chiên"))


def test_add_item_empty_name_raises():
    svc = MenuService()
    with pytest.raises(ValueError, match="Tên món không được để trống"):
        svc.add_item(MenuItem(item_id="M01", name="   ", price=20000.0, category="Cơm chiên"))


def test_update_item(service: MenuService):
    service.update_item("M01", name="Cơm chiên Dương Châu Đặc Biệt", price=45000.0)
    item = service.get_item("M01")
    assert item.name == "Cơm chiên Dương Châu Đặc Biệt"
    assert item.price == 45000.0


def test_update_nonexistent_item_raises(service: MenuService):
    with pytest.raises(KeyError):
        service.update_item("UNKNOWN", price=50000.0)


def test_set_availability(service: MenuService):
    service.set_availability("M01", False)
    assert service.get_item("M01").available is False
    avail_list = service.list_all(only_available=True)
    assert all(it.item_id != "M01" for it in avail_list)


def test_delete_item(service: MenuService):
    assert service.delete_item("M01") is True
    assert service.get_item("M01") is None
    with pytest.raises(KeyError):
        service.delete_item("M01")


def test_search_by_name(service: MenuService):
    res = service.search_by_name("hải sản")
    assert len(res) == 1
    assert res[0].item_id == "M02"

    res_all = service.search_by_name("cơm")
    assert len(res_all) == 2


def test_filter_by_category(service: MenuService):
    drinks = service.filter_by_category("Đồ uống")
    assert len(drinks) == 1
    assert drinks[0].item_id == "D01"
