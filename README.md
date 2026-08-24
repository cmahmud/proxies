# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 382
- HTTP: 108 alive / 45 gold
- HTTPS: 43 alive / 10 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 180 alive / 166 gold

## Historical pool

- Discovered: 180671
- Ever alive: 33580
- Ever gold: 1242

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
