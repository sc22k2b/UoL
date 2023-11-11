/*import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.chart.LineChart;
import javafx.scene.chart.NumberAxis;
import javafx.scene.chart.XYChart;
import javafx.stage.Stage;*/


/**
 * JavaFX application to plot elevations of a GPS track, for
 * the Advanced task of COMP1721 Coursework 1.
 *
 * @author YOUR NAME HERE
 */
/*public class PlotApplication extends Application {
  // OPTIONAL: Implement the elevation plotting application here
  @Override public void start(Stage stage){

    if(args.length != 1){
        System.out.println("No file name given");
        System.exit(0);
    }

    Track tempTrack = new Track(args[0]);

    stage.setTitle("Plotted elevation graph");
    NumberAxis xAxis = new NumberAxis();
    xAxis.setLabel("Distance (m)");

    NumberAxis yAxis = new NumberAxis();
    yAxis.setLabel("Elevation (m)");

    LineChart linechart = new LineChart(xAxis, yAxis);

    double[] distances = new double[tempTrack.pointSequence.size()-1];

    for(int i = 0; i<tempTrack.pointSequence.size()-1; i++){
        distances[i] = Point.greatCircleDistance(tempTrack.pointSequence.get(i),tempTrack.pointSequence.get(i+1));
    }

    lineChart.setName("Elevation plot");
    XYChart.Series series = new XYChartSeries();

    for(int count = 0; count<tempTrack.pointSequence.size()-1; count++){
        series.getData().add(new XYChart.Data(distances[count], tempTrack.get(count).elevation));
        }

    Scene scene = new Scene(lineChart,1000,800);
    lineChart.getData().add(series);

    stage.setScene(scene);
    stage.show();

    
  }

  public static void main(String[] args){
    launch(args)
    
}
}*/
