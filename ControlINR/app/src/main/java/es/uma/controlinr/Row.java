package es.uma.controlinr;

import android.graphics.drawable.Drawable;

/**
 * Created by Francisco on 30/04/2017.
 */

public class Row {
    private String text, image;
    private int color;

    public Row(String t, String  i, int c){
        this.text = t;
        this.image = i;
        this.color = c;
    }

    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }

    public int getColor() {
        return color;
    }

    public void setColor(int color) {
        this.color = color;
    }
}
