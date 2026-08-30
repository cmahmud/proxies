# SyndProxy validated proxy pool

## Current pool

- Alive now: 534
- Gold now: 435
- HTTP: 105 alive / 80 gold
- HTTPS: 62 alive / 25 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 199 alive / 168 gold

## Historical pool

- Discovered: 199830
- Ever alive: 44560
- Ever gold: 1406

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
