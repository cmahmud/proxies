# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 429
- HTTP: 108 alive / 75 gold
- HTTPS: 55 alive / 25 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 189 alive / 167 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44455
- Ever gold: 1399

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
