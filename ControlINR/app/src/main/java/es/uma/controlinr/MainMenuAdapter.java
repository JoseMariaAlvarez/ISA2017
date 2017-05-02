package es.uma.controlinr;

import android.content.Context;
import android.content.res.Resources;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;

import es.uma.controlinr.R;

import java.util.ArrayList;

/**
 * Created by Francisco on 30/04/2017.
 */

public class MainMenuAdapter extends BaseAdapter {

    private ArrayList<Row> rowList;
    private LayoutInflater lInflater;
    private Resources resources;

    public MainMenuAdapter(Context context, ArrayList<Row> list){
        this.lInflater = LayoutInflater.from(context);
        this.rowList = list;
    }

    @Override
    public int getCount() {
        return rowList.size();
    }

    @Override
    public Object getItem(int i) {
        return rowList.get(i);
    }

    @Override
    public long getItemId(int i) {
        return i;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {

        ViewContainer container = null;
        if (view == null) {
            view = lInflater.inflate(R.layout.row_main_menu, null);

            container = new ViewContainer();
            container.text = (TextView) view.findViewById(R.id.tv_patient_text);
            container.image = (ImageView) view.findViewById(R.id.iv_patient_image);
            container.layout = (LinearLayout) view.findViewById(R.id.ll_row);

            view.setTag(container);
        } else
            container = (ViewContainer) view.getTag();

        Row r = (Row) getItem(i);

        container.text.setText(r.getText());
        container.image.setImageBitmap(
                decodeSampledBitmapFromResource(view.getResources(),
                        view.getResources().getIdentifier(r.getImage(), "drawable", lInflater.getContext().getPackageName()),
                        100, 100));
        container.layout.setBackgroundColor(r.getColor());
        return view;
    }

    class ViewContainer{
        TextView text;
        ImageView image;
        LinearLayout layout;
    }

    public static int calculateInSampleSize(
            BitmapFactory.Options options, int reqWidth, int reqHeight) {
        // Raw height and width of image
        final int height = options.outHeight;
        final int width = options.outWidth;
        int inSampleSize = 1;

        if (height > reqHeight || width > reqWidth) {

            final int halfHeight = height / 2;
            final int halfWidth = width / 2;

            // Calculate the largest inSampleSize value that is a power of 2 and keeps both
            // height and width larger than the requested height and width.
            while ((halfHeight / inSampleSize) >= reqHeight
                    && (halfWidth / inSampleSize) >= reqWidth) {
                inSampleSize *= 2;
            }
        }

        return inSampleSize;
    }

    public static Bitmap decodeSampledBitmapFromResource(Resources res, int resId, int reqWidth, int reqHeight) {

        // First decode with inJustDecodeBounds=true to check dimensions
        final BitmapFactory.Options options = new BitmapFactory.Options();
        options.inJustDecodeBounds = true;
        BitmapFactory.decodeResource(res, resId, options);

        // Calculate inSampleSize
        options.inSampleSize = calculateInSampleSize(options, reqWidth, reqHeight);

        // Decode bitmap with inSampleSize set
        options.inJustDecodeBounds = false;
        return BitmapFactory.decodeResource(res, resId, options);
    }
}
