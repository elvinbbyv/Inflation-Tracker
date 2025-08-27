import pandas as pd
import matplotlib.pyplot as plt

#Loading CSV file
def load_csv():
    df = pd.read_csv("write your csv file location")
    print("CSV file successfully loaded.")
    return df

#Displaying file info
def show_file_info(df):
    print("\n--- FILE INFO ---")
    print(df.info())

#Displaying rows and columns
def show_shape(df):
    print(f"\nTotal Rows: {df.shape[0]}") #Rows
    print(f"Total Columns: {df.shape[1]}") #Columns

#Displaying first 10 rows and columns
def show_first10(df):
    pd.set_option("display.max_columns", None) #For showing all columns
    print(df.head(10))

#Performing Basic statistics
def basic_statistics(df):
    print("\n--- BASIC STATISTICS ---")
    print("Mean:\n", df.mean(numeric_only=True))
    print("Median:\n", df.median(numeric_only=True))
    print("Min:\n", df.min(numeric_only=True))
    print("Max:\n", df.max(numeric_only=True))

#Cleaning data, handling missing values and duplicates
def clean_data(df):
    print("\n--- CLEANING DATA ---")
    print("Missing values before:\n", df.isnull().sum())
    df_cleaned = df.fillna(df.mean(numeric_only=True))
    df_cleaned = df_cleaned.drop_duplicates()
    print("Missing values after:\n", df_cleaned.isnull().sum())
    return df_cleaned

#Showing graphs using matplotlib
def show_graphs(df):
    while True:
        print("\n--- GRAPH MENU ---")
        print("1. Line Chart - Average CPI Over Years")
        print("2. Bar Chart - Average Inflation by Country")
        print("3. Bar Chart - Average Unemployment Over Years")
        print("0. Return to Main Menu")

        graph_choice = input("Choose an option: ")

        if graph_choice == "1":
            cpi_by_year = df.groupby("Year")["CPI"].mean()
            plt.plot(cpi_by_year.index, cpi_by_year.values, marker='o', color='orange')
            plt.title("Average CPI Over Years")
            plt.xlabel("Year")
            plt.ylabel("CPI")
            plt.grid(True)
            plt.tight_layout()
            plt.show()

        elif graph_choice == "2":
            avg_inflation = df.groupby("Country")["Annual_Inflation"].mean().sort_values(ascending=False).head(10)
            avg_inflation.plot(kind="bar", color="skyblue")
            plt.title("Top 10 Countries by Average Annual Inflation")
            plt.xlabel("Country")
            plt.ylabel("Average Annual Inflation")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.show()

        elif graph_choice == "3":
            avg_unemp = df.groupby("Year")["Unemployment_Rate"].mean()
            avg_unemp.plot(kind="bar", color="lightgreen")
            plt.title("Average Unemployment Rate Over Years")
            plt.xlabel("Year")
            plt.ylabel("Unemployment Rate (%)")
            plt.tight_layout()
            plt.show()

        elif graph_choice == "0":
            break

        else:
            print("Invalid option. Please choose again.")




#Exporting cleaned data and summary to csv and txt file format
def export_results(df):
    df.to_csv("cleaned_data.csv", index=False)
    print("Cleaned data saved to 'cleaned_data.csv'.")

    with open("summary_report.txt", "w") as f:
        f.write("SUMMARY REPORT\n")
        f.write("====================\n")
        f.write(f"Rows: {df.shape[0]}\nColumns: {df.shape[1]}\n\n")
        f.write("Column Names and Types:\n")
        f.write(str(df.dtypes))
        f.write("\n\nBasic Statistics:\n")
        f.write(str(df.describe()))
    print("Summary report saved to 'summary_report.txt'.")

#Top 5 countries by average inflation
def top5_countries_by_inflation(df):
    print("\n--- TOP 5 COUNTRIES BY AVERAGE ANNUAL INFLATION ---")
    group = df.groupby("Country")["Annual_Inflation"].mean()
    top5 = group.sort_values(ascending=False).head(5)
    print(top5)

#Main menu loop for selecting operations
def run_interface(df_original):
    df_cleaned = None  #Start with no cleaned data

    while True:
        print("\n--- CSV Data Analyzer ---")
        print("1. Show file info")
        print("2. Show total rows and columns")
        print("3. Show basic statistics")
        print("4. Clean the data")
        print("5. Show graphs")
        print("6. Export cleaned data and summary report")
        print("7. Show Top 5 Countries by Average Annual Inflation")
        print("8. Show first 10 rows and columns")
        print("0. Exit")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                if df_cleaned is not None:
                    show_file_info(df_cleaned)
                else:
                    show_file_info(df_original)

            case "2":
                if df_cleaned is not None:
                    show_shape(df_cleaned)
                else:
                    show_shape(df_original)

            case "3":
                if df_cleaned is not None:
                    basic_statistics(df_cleaned)
                else:
                    basic_statistics(df_original)

            case "4":
                df_cleaned = clean_data(df_original)

            case "5":
                if df_cleaned is not None:
                    show_graphs(df_cleaned)
                else:
                    show_graphs(df_original)

            case "6":
                pd.set_option("display.max_columns", None) #For exporting all columns
                if df_cleaned is not None:
                    export_results(df_cleaned)
                else:
                    export_results(df_original)

            case "7":
                if df_cleaned is not None:
                    top5_countries_by_inflation(df_cleaned)
                else:
                    top5_countries_by_inflation(df_original)

            case "8":
                if df_cleaned is not None:
                    show_first10(df_cleaned)
                else:
                    show_first10(df_original)

            case "0":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please try again.")

#Starting the program
df_main = load_csv()
run_interface(df_main)

