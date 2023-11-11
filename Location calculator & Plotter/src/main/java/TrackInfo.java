/**
 * Program to provide information on a GPS track stored in a file.
 *
 * @author Kian Barry
 */
public class TrackInfo {
  public static void main(String[] args) {
    // TODO: Implement TrackInfo application here

    
    //Ensures the user has given the correct number of arguments (1 - the file name)
    if(args.length != 1){
        System.out.println("No file name given");
        System.exit(0);
    }

    try{
        //Constructs a new point using what was supplied in the command line argument
        Track track = new Track(args[0]);

        //Allocates values to variables in track using the methods built
        track.numOfTracks = track.size();
        track.lowestPoint = track.lowestPoint();
        track.highestPoint = track.highestPoint();
        track.totalDistance = track.totalDistance();
        track.averageSpeed = track.averageSpeed();

        //Displays the information just allocated to the user
        System.out.println(track.numOfTracks + " points in track");
        System.out.println("Lowest point is " + track.lowestPoint);
        System.out.println("Highest point is " + track.highestPoint);
        System.out.println("Total distance = " + track.totalDistance + " km");
        System.out.println("Average speed = " + track.averageSpeed + " m/s");
    }
    catch(Exception e){
        System.exit(0);
    }

  }
}
