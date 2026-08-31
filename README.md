# SyndProxy validated proxy pool

## Current pool

- Alive now: 598
- Gold now: 438
- HTTP: 124 alive / 77 gold
- HTTPS: 98 alive / 26 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 199 alive / 173 gold

## Historical pool

- Discovered: 199830
- Ever alive: 45461
- Ever gold: 1433

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
