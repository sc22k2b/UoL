/**
 * Program to general a KML file from GPS track data stored in a file,
 * for the Advanced task of COMP1721 Coursework 1.
 *
 * @author Kian Barry
 */
public class ConvertToKML {
  public static void main(String[] args) {
    try{
        //Constructs a new track with the data in the text file given
        Track tempTrack = new Track(args[0]);

        //Writes the data acquired to a KML file with the correct formatting
        tempTrack.writeKML(args[1]);
        
    }
    catch(Exception e){

        System.exit(1);
    }
    
  }
}
