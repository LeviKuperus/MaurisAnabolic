/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package samplecourse8;

import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import javax.swing.JOptionPane;

/**
 *
 * @author Patrick
 */
public class SampleCourse8 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws IOException, URISyntaxException {
        sample();
        
    }

    private static void sample() throws IOException, URISyntaxException {
        String invoer = JOptionPane.showInputDialog("Voer eiwit in");
        Desktop bureau=Desktop.getDesktop();
        bureau.browse(new URI("http://www.ncbi.nlm.nih.gov/pubmed/?term="+invoer));
    }
    
}
