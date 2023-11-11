import java.time.ZonedDateTime;

import static java.lang.Math.abs;
import static java.lang.Math.atan2;
import static java.lang.Math.cos;
import static java.lang.Math.sin;
import static java.lang.Math.sqrt;
import static java.lang.Math.toRadians;


/**
 * Represents a point in space and time, recorded by a GPS sensor.
 *
 * @author Nick Efford & Kian Barry
 */
public class Point {
  // Constants useful for bounds checking, etc

  private static final double MIN_LONGITUDE = -180.0;
  private static final double MAX_LONGITUDE = 180.0;
  private static final double MIN_LATITUDE = -90.0;
  private static final double MAX_LATITUDE = 90.0;
  private static final double MEAN_EARTH_RADIUS = 6.371009e+6;

  //Variables:

  public ZonedDateTime time;
  public double longitude;
  public double latitude;
  public double elevation;

  // TODO: Create a stub for the constructor

    public Point(ZonedDateTime t, double lon, double lat, double elev){

        time = t;

        
        setLongitude(lon);

        
        setLatitude(lat);

        elevation = elev;


    }

    private void setLongitude(double lon){

        //Checks to see if the longitude given exceeds the maximum or minimum values (throws an exception if they are) and assigns the value to the longitude variable if it is within the parameters
        if(lon<MAX_LONGITUDE){
            if(lon>MIN_LONGITUDE){
                longitude = lon;
            }
            else{
                throw new GPSException("Longitude too small");
            }

        }
        else{
            throw new GPSException("Longitude too big");
        }

    }

    private void setLatitude(double lat){

        //Checks to see if the latitude given exceeds the maximum or minimum values (throws an exception if they are) and assigns the value to the latitude variable if it is within the parameters
        if(lat<MAX_LATITUDE){
            if(lat>MIN_LATITUDE){
                
                latitude = lat;
            }
            else{
                throw new GPSException("Latitude too small");
            }

        }
        else{
            throw new GPSException("Latitude too big");
        }

    }

  // TODO: Create a stub for getTime()

    public ZonedDateTime getTime(){

        return time;

    }

  // TODO: Create a stub for getLatitude()

    public double getLatitude(){

        return latitude;

    }

  // TODO: Create a stub for getLongitude()

    public double getLongitude(){

        return longitude;
        
    }

  // TODO: Create a stub for getElevation()

    public double getElevation(){

        return elevation;
    }

  // TODO: Create a stub for toString()

    public String toString(){

        //Constructs a string using the values supplied

        String tempString = "(" + (double)Math.round(longitude*100000)/100000 + ", " + (double)Math.round(latitude*100000)/100000 + "), " + (double)Math.round(elevation*10)/10 + " m";
        
        return tempString;
    }

  // IMPORTANT: Do not alter anything beneath this comment!

  /**
   * Computes the great-circle distance or orthodromic distance between
   * two points on a spherical surface, using Vincenty's formula.
   *
   * @param p First point
   * @param q Second point
   * @return Distance between the points, in metres
   */
  public static double greatCircleDistance(Point p, Point q) {
    double phi1 = toRadians(p.getLatitude());
    double phi2 = toRadians(q.getLatitude());

    double lambda1 = toRadians(p.getLongitude());
    double lambda2 = toRadians(q.getLongitude());
    double delta = abs(lambda1 - lambda2);

    double firstTerm = cos(phi2)*sin(delta);
    double secondTerm = cos(phi1)*sin(phi2) - sin(phi1)*cos(phi2)*cos(delta);
    double top = sqrt(firstTerm*firstTerm + secondTerm*secondTerm);

    double bottom = sin(phi1)*sin(phi2) + cos(phi1)*cos(phi2)*cos(delta);

    return MEAN_EARTH_RADIUS * atan2(top, bottom);
  }
}
