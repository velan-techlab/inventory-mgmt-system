package org.service.inventory.model;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Inventory {

    @Id
    @Column(name = "item_id")
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long itemId;
    @Column(name = "item_name")
    private String itemName;
    @Column(name = "quantity") 
    private int quantity;
    @Column(name = "price")
    private double price;
    public Long getItemId() {
        return itemId;
    }
    public String getItemName() {
        return itemName;
    }
    public int getQuantity() {
        return quantity;
    }
    public double getPrice() {
        return price;
    }
    public void setItemId(Long itemId) {
        this.itemId = itemId;
    }
    public void setItemName(String itemName) {
        this.itemName = itemName;
    }
    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public void setPrice(double price) {
        this.price = price;
    }
    public Inventory(String itemName, int quantity, double price) {
        this.itemName = itemName;
        this.quantity = quantity;
        this.price = price;
    }
    public Inventory() {
    }
    
    @Override
    public String toString() {
        return "Inventory [itemId=" + itemId + ", itemName=" + itemName + ", quantity=" + quantity + ", price=" + price
                + "]";
    }
}

