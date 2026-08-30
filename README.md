# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 433
- HTTP: 103 alive / 79 gold
- HTTPS: 60 alive / 25 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 204 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44557
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
