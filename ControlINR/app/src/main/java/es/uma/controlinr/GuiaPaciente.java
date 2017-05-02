package es.uma.controlinr;

import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.widget.ExpandableListView;

import com.example.juanignacio.controlinr.R;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * Created by Juan Ignacio on 25/04/2017.
 */
public class GuiaPaciente extends AppCompatActivity {

    private List<String> listDataHeader;
    private HashMap<String,List<String>> listHash;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_guiapaciente);
        initdata();
        ExpandableListView boton = (ExpandableListView) findViewById(R.id.ExpPaciente);
        ExpandableListAdapter expandable = new ExpandableListAdapter(this, listDataHeader, listHash);
        boton.setAdapter(expandable);
    }

    private void initdata(){
        listDataHeader = new ArrayList<>();
        listHash = new HashMap<>();

        listDataHeader.add(getString(R.string.aco));
        listDataHeader.add(getString(R.string.quienes_aco));
        listDataHeader.add(getString(R.string.administrar_aco));
        listDataHeader.add(getString(R.string.cantidad));
        listDataHeader.add(getString(R.string.donde_control));
        listDataHeader.add(getString(R.string.tiempo_control));
        listDataHeader.add(getString(R.string.dieta));
        listDataHeader.add(getString(R.string.oscilaciones));
        listDataHeader.add(getString(R.string.cuando_aco));
        listDataHeader.add(getString(R.string.error_dosis));
        listDataHeader.add(getString(R.string.complicaciones));
        listDataHeader.add(getString(R.string.sangrar));
        listDataHeader.add(getString(R.string.autocontrol));


        List<String> aco = new ArrayList<>();
        aco.add(getString(R.string.texto_aco));

        List<String> quienesAco = new ArrayList<>();
        quienesAco.add(getString(R.string.texto_quienes_aco));

        List<String> adminAco = new ArrayList<>();
        adminAco.add(getString(R.string.texto_administrar_aco));

        List<String> cantidad = new ArrayList<>();
        cantidad.add(getString(R.string.texto_cantidad));

        List<String> donde = new ArrayList<>();
        donde.add(getString(R.string.texto_donde_control));

        List<String> tiempo = new ArrayList<>();
        tiempo.add(getString(R.string.texto_tiempo_control));

        List<String> dieta = new ArrayList<>();
        dieta.add(getString(R.string.texto_dieta));

        List<String> oscilaciones = new ArrayList<>();
        oscilaciones.add(getString(R.string.texto_oscilaciones));

        List<String> cuandoAco = new ArrayList<>();
        cuandoAco.add(getString(R.string.texto_cuando_aco));

        List<String> errorDosis = new ArrayList<>();
        errorDosis.add(getString(R.string.texto_error_dosis));

        List<String> complicaciones = new ArrayList<>();
        complicaciones.add(getString(R.string.texto_complicaciones));

        List<String> sangrar = new ArrayList<>();
        sangrar.add(getString(R.string.texto_sangrar));

        List<String> autocontrol = new ArrayList<>();
        autocontrol.add(getString(R.string.texto_autocontrol));


        listHash.put(listDataHeader.get(0),aco);
        listHash.put(listDataHeader.get(1),quienesAco);
        listHash.put(listDataHeader.get(2),adminAco);
        listHash.put(listDataHeader.get(3),cantidad);
        listHash.put(listDataHeader.get(4),donde);
        listHash.put(listDataHeader.get(5),tiempo);
        listHash.put(listDataHeader.get(6),dieta);
        listHash.put(listDataHeader.get(7),oscilaciones);
        listHash.put(listDataHeader.get(8),cuandoAco);
        listHash.put(listDataHeader.get(9),errorDosis);
        listHash.put(listDataHeader.get(10),complicaciones);
        listHash.put(listDataHeader.get(11),sangrar);
        listHash.put(listDataHeader.get(12),autocontrol);

    }
}
