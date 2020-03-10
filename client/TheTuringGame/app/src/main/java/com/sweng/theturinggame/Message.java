package com.sweng.theturinggame;

import java.util.Date;

public class Message {

    private int id;
    private String text;
    private Date timestamp;

    public Message(int id, String text, Date timestamp) {
        this.id = id;
        this.text = text;
        this.timestamp = timestamp;
    }

    @Override
    public String toString() {
        return text;
    }

}
