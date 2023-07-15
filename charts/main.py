import charts
import readcsv
import utils


def main():
    data = readcsv.read_csv('data.csv')
    country = input('Enter a country: ')

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        labels, values = utils.generate_population_by_country(result[0])
        charts.generate_bar_chart(country, labels, values)
    else:
        print('Country not found')


if __name__ == '__main__':
    main()
