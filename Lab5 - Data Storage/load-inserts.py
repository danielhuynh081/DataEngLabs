import csv
import psycopg2
import argparse

def create_table(cur):
    cur.execute("""
        DROP TABLE IF EXISTS census;
        CREATE TABLE census (
            tract_id TEXT PRIMARY KEY,
            state TEXT,
            county TEXT,
            total_pop INTEGER,
            men INTEGER,
            women INTEGER,
            hispanic REAL,
            white REAL,
            black REAL,
            native REAL,
            asian REAL,
            pacific REAL,
            voting_age_citizen INTEGER,
            income REAL,
            income_err REAL,
            income_per_cap REAL,
            income_per_cap_err REAL,
            poverty REAL,
            child_poverty REAL,
            professional REAL,
            service REAL,
            office REAL,
            construction REAL,
            production REAL,
            drive REAL,
            carpool REAL,
            transit REAL,
            walk REAL,
            other_transp REAL,
            work_at_home REAL,
            mean_commute REAL,
            employed INTEGER,
            private_work REAL,
            public_work REAL,
            self_employed REAL,
            family_work REAL,
            unemployment REAL
        );
    """)

def insert_data_copy(cur, csv_file):
    print(f"Loading data from {csv_file} using copy_from()...")
    with open(csv_file, 'r') as f:
        next(f)  # Skip header row
        cur.copy_from(f, 'census', sep=',', null='', columns=(
            'tract_id', 'state', 'county', 'total_pop', 'men', 'women',
            'hispanic', 'white', 'black', 'native', 'asian', 'pacific',
            'voting_age_citizen', 'income', 'income_err',
            'income_per_cap', 'income_per_cap_err', 'poverty',
            'child_poverty', 'professional', 'service', 'office',
            'construction', 'production', 'drive', 'carpool',
            'transit', 'walk', 'other_transp', 'work_at_home',
            'mean_commute', 'employed', 'private_work', 'public_work',
            'self_employed', 'family_work', 'unemployment'
        ))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', action='store_true', help='Create table')
    parser.add_argument('-d', required=True, help='CSV file path')
    args = parser.parse_args()

    conn = psycopg2.connect(
        dbname='postgres', user='postgres', password='hv4Fq-na8z', host='localhost'
    )
    cur = conn.cursor()

    if args.c:
        print("Creating table...")
        create_table(cur)

    insert_data_copy(cur, args.d)
    conn.commit()

    cur.close()
    conn.close()
    print("Done.")

if __name__ == '__main__':
    main()

