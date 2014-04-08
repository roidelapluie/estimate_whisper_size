import sys

mod = {
        's' : 1,
        'm' : 60,
        'h' : 3600,
        'd' : 86400,
        'w' : 86400 * 7,
        'y' : 86400 * 365
}
retention=sys.argv[1]

ranges = retention.split(',')
total = 0.
for metrics in ranges:
    keep,duration = metrics.split(':')
    durationn=duration[:-1]
    durationl=duration[-1]
    keepn=keep[:-1]
    keepl=keep[-1]
    tokeep = mod[keepl]*int(keepn)
    tokeepduration = mod[durationl]*int(durationn)
    total+=tokeepduration/tokeep
print round(total /315360000.*3695632),'k'
