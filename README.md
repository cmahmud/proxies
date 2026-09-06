# SyndProxy validated proxy pool

## Current pool

- Alive now: 428
- Gold now: 363
- HTTP: 68 alive / 53 gold
- HTTPS: 27 alive / 11 gold
- SOCKS4: 161 alive / 150 gold
- SOCKS5: 172 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48255
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
