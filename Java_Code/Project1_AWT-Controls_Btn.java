import java.awt.*;
import java.awt.event.*;
public class SubjectDetails extends Frame {
    public SubjectDetails() {
        setTitle(" DATE-Feb/02/2025 , Today's Class Details ");
        setSize(600, 280);
        setLayout(new FlowLayout());
        setBackground(Color.pink);
        Button btnpython = new Button("Python");
        Button btnEnglish = new Button("English");
        Button btnKannada = new Button("Kannada");
        Button btnPHP = new Button("PHP");
        Button btnCN = new Button("Computer Networks ");
        Button btnOK = new Button("Okay ");
        Label labelDetails = new Label("");
        labelDetails.setAlignment(Label.CENTER);
        btnOK.setPreferredSize(new Dimension(80,35));
        labelDetails.setPreferredSize(new Dimension(800, 300));
        add(btnpython);
        add(btnEnglish);
        add(btnKannada);
        add(btnPHP);
        add(btnCN);
        add(btnOK);
        add(labelDetails);
        btnpython.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                labelDetails.setText(
                        "Class-1 , Time-9AM to 10AM , Topics Covered-Arrays ");
          }
        });
        btnEnglish.addActionListener(new ActionListener() {
             public void actionPerformed(ActionEvent e) {
                labelDetails.setText("Class-2 , Time-10AM to 11AM , Topics Covered-Unit-2 ");
            }
        });
        btnKannada.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                labelDetails.setText("Class-3  , Time-12PM to 1PM , Topics Covered-Unit-1 ");
            }
        });
        btnPHP.addActionListener(new ActionListener() {
        public void actionPerformed(ActionEvent e) {
                labelDetails.setText("Class-4, Time-2PM to 3PM , Topics Covered-Installation and Configuration ");
            }
        });
        btnCN.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                labelDetails.setText("Class-5 , Time-3 PM to 4 PM , Topics Covered- Topology and its Types ");
            }
        });
        btnOK.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                labelDetails.setText("Be on time !! , See you in class ");
                System.exit(0);
            }
        });
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
        setVisible(true);
    }
    public static void main(String[] args) {
        new SubjectDetails();
    }
    }
