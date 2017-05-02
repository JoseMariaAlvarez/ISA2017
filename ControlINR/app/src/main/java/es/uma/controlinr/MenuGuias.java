package es.uma.controlinr;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

import es.uma.controlinr.R;

/**
 * Created by Juan Ignacio on 25/04/2017.
 */
public class MenuGuias extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_menuguias);

        /*
        List<Row> elements = new ArrayList<Row>();
        elements.add(new Row(getString(R.string.calendar), getString(R.string.calendar_icon), R.color.color1));
        elements.add(new Row(getString(R.string.guide), getString(R.string.guide_icon), R.color.color2));
        elements.add(new Row(getString(R.string.graphs), getString(R.string.graphic_icon), R.color.color3));
        elements.add(new Row(getString(R.string.meals), getString(R.string.meals_icon), R.color.color4));
        elements.add(new Row(getString(R.string.automedication), getString(R.string.automed_icon), R.color.color5));
        elements.add(new Row(getString(R.string.alarm), getString(R.string.alarm_icon), R.color.color6));
        MainMenuAdapter adapter = new MainMenuAdapter(this, (ArrayList<Row>) elements);
        ListView lv = (ListView) findViewById(android.R.id.list);
        lv.setAdapter((adapter));
        */

    }

}