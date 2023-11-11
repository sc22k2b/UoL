/**
 * Represents a point in space and time, recorded by a GPS sensor.
 *
 * @author Kian Barry
 */
import java.util.List;
import java.util.ArrayList;
import java.io.*;
import java.util.Scanner;
import java.time.ZonedDateTime;
import java.time.temporal.ChronoUnit;


public class Track {
  // TODO: Create a stub for the constructor

    List<Point> pointSequence = new ArrayList<Point>();

    public int numOfTracks;
    public Point highestPoint;
    public Point lowestPoint;
    public double totalDistance;
    public double averageSpeed;

    public Track(){

    }

    public Track(String filename) throws IOException{

        
        readFile(filename);

    }

  // TODO: Create a stub for readFile()

  public void readFile(String filename) throws FileNotFoundException{

    //Retrieves file and stores it as a File variable
    File existFile =  new File(filename);

    //Checks to see the file exists and throws an exception if not
        if(existFile.exists() == false){
            throw new FileNotFoundException("File does not exist");   
        }

    //Removes any data from the previous file
    pointSequence.removeAll(pointSequence);


    try{

        //Sets up a file input stream and reads the contents of the file 
        FileInputStream readingFile = new FileInputStream(filename);
        Scanner data = new Scanner(readingFile);
        int headerCount = 0;

        //Continues to loop whilst there is still a next line in the file
        while(data.hasNextLine()){

            String[] splitData = data.nextLine().split(",");

            /*if(splitData.length != 4){
                throw new GPSException("Not enough columns");
            }*/
            //Checks to see that the array holds 4 items of data (As this is the Longitude, Latitude, Elevation and Time) and throws an exception if not
            if(splitData.length == 4){
                if(headerCount>0){

                    double tempLongitude = Double.parseDouble(splitData[1]);
                    double tempLatitude = Double.parseDouble(splitData[2]);
                    double tempElevation = Double.parseDouble(splitData[3]);
                    Point tempPoint = new Point(ZonedDateTime.parse(splitData[0]), tempLongitude, tempLatitude, tempElevation);

                    //Adds the new point to the array list
                    pointSequence.add(tempPoint);
                }
            }
            else{
                throw new GPSException("Not enough columns");
            }
            headerCount++;
        }
        

    }
    catch(IOException e){


    }

  }

  // TODO: Create a stub for add()

  public void add(Point point){

        pointSequence.add(point);
  }

  // TODO: Create a stub for get()

  public Point get(int index){

    //Validates that the array list holding the points isn't empty, of negative size or be smaller than the requested index as this would make the get request invalid, throws an excpetion in any of these cases
    if(pointSequence.isEmpty()){

        throw new GPSException("Nothing to get, Track is empty");
    }
    
    if(index < 0){
        
        throw new GPSException("Index too low");
    }

    if(index >= pointSequence.size()){

        throw new GPSException("Index is too high");
    }

    //Gets the point in the point sequence at the corresponding index
    return pointSequence.get(index);
  }

  // TODO: Create a stub for size()

  public int size(){

    return pointSequence.size();
  }

  // TODO: Create a stub for lowestPoint()

  public Point lowestPoint(){

    if(pointSequence.isEmpty()){

        throw new GPSException("No lowest point as there is an empty Track");
    }

    int lowestPoint = 0;

    //Loops through the array list and updates lowest point depending on which index has the smallest elevation
    for(int i = 0; i<pointSequence.size()-1; i++){

        //Creates two point objects to hold the point at the current index and the point at the next index (so they can be compared)
        Point tempPoint = pointSequence.get(i);
        Point tempPointNextIncrement = pointSequence.get(i+1);

        if(tempPoint.elevation>tempPointNextIncrement.elevation){

            //Changes the lowest point to the point at the next index as it had a lower elevation to the point at the current index(i)
            lowestPoint = i+1;
        }
        else{

            lowestPoint = i;
        }
    }

    //Returns the point that has the smallest elevation
    return pointSequence.get(lowestPoint);
  }

  // TODO: Create a stub for highestPoint()

  public Point highestPoint(){

    if(pointSequence.isEmpty()){

        throw new GPSException("No highest point as there is an empty Track");
    }
    int highestPoint = 0;

    //Loops through the array list and updates highest point depending on which index has the highest elevation
    for(int i = 0; i<pointSequence.size()-1; i++){

        //Creates two point objects to hold the point at the current index and the point at the next index (so they can be compared)
        Point tempPoint = pointSequence.get(highestPoint);
        Point tempPointNextIncrement = pointSequence.get(i+1);

        if(tempPoint.elevation < tempPointNextIncrement.elevation){

            //Changes the highest point to the index of the next increment as the point at that index has a higher elevation than the point at the current index (i)
            highestPoint = i+1;
        }
    
    }

    //Returns the point that has the highest elevation
    return pointSequence.get(highestPoint);
  }

  // TODO: Create a stub for totalDistance()

  public double totalDistance(){

    //Checks to see point sequence is large enough to compute the total distance - throws an exception explaining more than 2 points are needed if not
    if(pointSequence.size()<2){
        throw new GPSException("At least 2 points are needed to compute distance");
    } 
    double distanceTotal = 0;
    //Loops through the array list and calculates the distance between each point and then adds them together to get the totoal distance
    for(int i = 0; i<pointSequence.size()-1; i++){

        double distance = Point.greatCircleDistance(pointSequence.get(i),pointSequence.get(i+1));
        distanceTotal = distanceTotal + distance;
    }
    return distanceTotal;
  }

  // TODO: Create a stub for averageSpeed()

  public double averageSpeed(){

    //Checks to see point sequence is large enough to compute the average speed - throws an exception explaining more than 2 points are needed if not
    if(pointSequence.size()<2){
        throw new GPSException("At least 2 points are needed to compute average speed");
    }   
    
    //Uses the between functionality to calculate the time between the first and last point in the array list
    double timeBetweenPoints = ChronoUnit.SECONDS.between(pointSequence.get(0).time, pointSequence.get(pointSequence.size()-1).time);

    double speedAverage = totalDistance()/timeBetweenPoints;

    return speedAverage;
  }

  public void writeKML(String filename){

    try{
        //The filewriter writes all the KML data to the file - using the newline character (\n) to seperate them
        FileWriter fw = new FileWriter(filename);
        fw.write("<?xml version=\"1.0\"");
        fw.write(" encoding=\"UTF-8\"?>\n");
        fw.write("<kml xmlns=\"http://www.opengis.net/kml/2.2\">\n");
        fw.write("<Document>\n");
        fw.write("<Placemark>\n");
        fw.write("<LineString>\n");
        fw.write("<coordinates>\n");

        for(int i = 0; i<pointSequence.size()-1; i++){ //Loops through the track and writes the latitude and longitude of each point

            Point tempPoint = pointSequence.get(i);
            fw.write(tempPoint.longitude + "," + tempPoint.latitude + "\n");

        }

        //All the KML tags are closes
        fw.write("</coordinates>\n");
        fw.write("</LineString>\n");
        fw.write("</Placemark>\n");
        fw.write("</Document>\n");
        fw.write("</kml>");
        
        //The file is closed
        fw.close();
    }
    catch(Exception e){

        System.exit(1);
    }
  }
  
}
