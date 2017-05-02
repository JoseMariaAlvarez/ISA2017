package com.example.juanignacio.controlinr;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;

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

    /** Es llamado cuando el usuario hace click sobre el botón Paciente */
    public void abrirPaciente(View v) {
        Intent intent =new Intent(this, GuiaPaciente.class);
        startActivity(intent);
    }

    /** Es llamado cuando el usuario hace click sobre el botón Profesional */
    public void abrirProfesional(View v) {
        Intent intent =new Intent(this, GuiaProfesional.class);
        startActivity(intent);
    }

    /** Es llamado cuando el usuario hace click sobre el botón Emergencia */
    public void abrirEmergencia(View v) {
        Intent intent =new Intent(this, GuiaEmergencia.class);
        startActivity(intent);
    }
}