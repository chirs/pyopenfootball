import re
import datetime

def parse_results(lines, year):

    date = None
    results = []
    round = None

    for line in lines:
        #import pdb; pdb.set_trace()
        if line.startswith("#"):
            pass

        elif line.startswith("Matchday"):
            round = line.split('Matchday')[1].strip()

        elif line.startswith('['):
            date = parse_date(line, year)

        else:
            if line.strip():
                #import pdb; pdb.set_trace()
                
                r1 = re.match('(\d+\.\d+)(.*)', line)
                if r1:
                    time, line = r1.groups()
                else:
                    time = None

                ro = re.match('(.*)(\d+)\-(\d+)(.*)', line)
                home_team, home_score, away_score, away_team = ro.groups()
                result = {
                    'round': round,
                    'date': date,
                    'time': time,
                    'home_team': home_team.strip(),
                    'home_score': int(home_score),
                    'away_score': int(away_score),
                    'away_team': away_team.strip(),
                    }
                
                results.append(result)

    return results


def parse_date(s, year):
    months = {
        'Aug': 'August', 
        'Sept': 'September', 
        'Oct': 'October', 
        'Nov': 'November', 
        'Dec': 'December', 
        'Jan': 'January', 
        'Feb': 'February', 
        'Mar': 'March', 
        'Apr': 'April', 
        'May': 'May', 
        'Jun': 'June', 
        'Jul': 'July',
        }

    months = {
        'Aug': 8,
        'Sep': 9,
        'Sept': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12,
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        }
    
    s2 = s.replace('[', '').replace(']', '')
    a, b = s2.split(' ')
    m, d = b.split('/')
    day = int(d)
    month = months[m]

    d = datetime.date(year, month, day)
    return d
    

def main():
    f = open('/Users/chris/soccer/eng-england/2014-15/1-premierleague-i.txt').readlines()
    print(parse_results(f, 2014))
    

            
            
if __name__ == "__main__":
    main()

    
