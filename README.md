# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 436
- HTTP: 120 alive / 75 gold
- HTTPS: 89 alive / 27 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 205 alive / 172 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1433

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
