# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 433
- HTTP: 97 alive / 73 gold
- HTTPS: 63 alive / 29 gold
- SOCKS4: 175 alive / 161 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45471
- Ever gold: 1434

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
