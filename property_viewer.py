import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QTableWidget, QTableWidgetItem, QLabel

class MechanicalPropertyViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Reactor Data Viewer")
        self.setGeometry(100, 100, 1200, 600)

        # Define properties and associated tables
        self.properties = {
            "Manufacturing_Tube_Dimensions": [
                "reactor_data_min_thickness",
                "reactor_data_max_thickness",
                "reactor_data_min_inner_diameter",
                "reactor_data_max_inner_diameter",
                "reactor_data_avg_outside_diameter"
            ],
            "Manufacturing_Tube_Mechanical_Properties": ["Tube_Mechanical_Properties"],
            "Manufacturing_Tube_Chemical_Composition": ["Tube_Chemical_Composition"],
            "Manufacturing_Ingot_Details": ["Tube_Ingot_Details"],
            "Manufacturing_Installation": ["Tube_Installation"]
        }

        # Layout and widgets
        self.layout = QVBoxLayout()

        # Dropdown for selecting Mechanical Property
        self.property_label = QLabel("Select Mechanical Property:")
        self.property_dropdown = QComboBox()
        self.property_dropdown.addItems(self.properties.keys())
        self.property_dropdown.currentTextChanged.connect(self.update_table_dropdown)

        # Dropdown for selecting specific table within the selected property
        self.table_label = QLabel("Select Table:")
        self.table_dropdown = QComboBox()
        self.table_dropdown.currentTextChanged.connect(self.load_table_data)

        # Table widget to display data
        self.table_widget = QTableWidget()

        # Add widgets to layout
        self.layout.addWidget(self.property_label)
        self.layout.addWidget(self.property_dropdown)
        self.layout.addWidget(self.table_label)
        self.layout.addWidget(self.table_dropdown)
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

        # Initialize the table dropdown with the first property selection
        self.update_table_dropdown(self.property_dropdown.currentText())

    def update_table_dropdown(self, property_name):
        """Updates the table dropdown based on the selected property."""
        # Clear and populate the table dropdown
        self.table_dropdown.clear()
        tables = self.properties.get(property_name, [])
        self.table_dropdown.addItems(tables)

    def load_table_data(self):
        """Loads data from the selected table into the table widget."""
        table_name = self.table_dropdown.currentText()
        if not table_name:
            return

        # Connect to the database and fetch data
        connection = sqlite3.connect('reactor_data.db')
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Set up the table widget
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(column_names))
            self.table_widget.setHorizontalHeaderLabels(column_names)

            # Populate the table widget with data
            for row_index, row_data in enumerate(rows):
                for column_index, cell_data in enumerate(row_data):
                    cell_item = QTableWidgetItem(str(cell_data))
                    self.table_widget.setItem(row_index, column_index, cell_item)

            # Resize columns to fit content
            self.table_widget.resizeColumnsToContents()
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
        finally:
            # Close the database connection
            connection.close()
            
            
class ISIDataViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ISI Data Viewer")
        self.setGeometry(100, 100, 1200, 600)

        # Define ISI properties and associated tables
        self.properties = {
            "ISI Data Viewer": [
                "ISI_PSI_Avg_Diameter",
                "ISI_PT_Centerline_SAG",
                "ISI_Thickness",
                "ISI_Channel_Length",
                "ISI_Inspection_Log",
                "ISI_GS_Position"
            ]
        }

        # Layout and widgets
        self.layout = QVBoxLayout()

        # Dropdown for selecting ISI Property
        self.property_label = QLabel("Select ISI Property:")
        self.property_dropdown = QComboBox()
        self.property_dropdown.addItems(self.properties.keys())
        self.property_dropdown.currentTextChanged.connect(self.update_table_dropdown)

        # Dropdown for selecting specific table within the selected property
        self.table_label = QLabel("Select Table:")
        self.table_dropdown = QComboBox()
        self.table_dropdown.currentTextChanged.connect(self.load_table_data)

        # Table widget to display data
        self.table_widget = QTableWidget()

        # Add widgets to layout
        self.layout.addWidget(self.property_label)
        self.layout.addWidget(self.property_dropdown)
        self.layout.addWidget(self.table_label)
        self.layout.addWidget(self.table_dropdown)
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

        # Initialize the table dropdown with the first property selection
        self.update_table_dropdown(self.property_dropdown.currentText())

    def update_table_dropdown(self, property_name):
        """Updates the table dropdown based on the selected property."""
        # Clear and populate the table dropdown
        self.table_dropdown.clear()
        tables = self.properties.get(property_name, [])
        self.table_dropdown.addItems(tables)

    def load_table_data(self):
        """Loads data from the selected table into the table widget."""
        table_name = self.table_dropdown.currentText()
        if not table_name:
            return

        # Connect to the database and fetch data
        connection = sqlite3.connect('reactor_data.db')
        cursor = connection.cursor()
        try:
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Set up the table widget
            self.table_widget.setRowCount(len(rows))
            self.table_widget.setColumnCount(len(column_names))
            self.table_widget.setHorizontalHeaderLabels(column_names)

            # Populate the table widget with data
            for row_index, row_data in enumerate(rows):
                for column_index, cell_data in enumerate(row_data):
                    cell_item = QTableWidgetItem(str(cell_data))
                    self.table_widget.setItem(row_index, column_index, cell_item)

            # Resize columns to fit content
            self.table_widget.resizeColumnsToContents()
        except sqlite3.OperationalError as e:
            print(f"Error: {e}")
        finally:
            # Close the database connection
            connection.close()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #viewer = MechanicalPropertyViewer()
    viewer = ISIDataViewer()
    viewer.show()
    sys.exit(app.exec_())
