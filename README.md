# SyndProxy validated proxy pool

## Current pool

- Alive now: 542
- Gold now: 433
- HTTP: 108 alive / 79 gold
- HTTPS: 63 alive / 25 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 202 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44559
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
