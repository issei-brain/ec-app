from app import crud, models

def test_get_items_empty(test_db):
    items = crud.get_items(test_db)
    assert items == []

def test_get_items_with_records(test_db):
    item1 = models.Item(name="Item 1", category="Category 1", description="Description 1")
    item2 = models.Item(name="Item 2", category="Category 2", description="Description 2")
    
    test_db.add(item1)
    test_db.add(item2)
    test_db.commit()
    
    items = crud.get_items(test_db)
    
    assert len(items) == 2
    assert items[0].name == "Item 1"
    assert items[1].name == "Item 2"