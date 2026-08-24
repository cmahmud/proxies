# SyndProxy validated proxy pool

## Current pool

- Alive now: 505
- Gold now: 379
- HTTP: 123 alive / 53 gold
- HTTPS: 39 alive / 11 gold
- SOCKS4: 168 alive / 156 gold
- SOCKS5: 175 alive / 159 gold

## Historical pool

- Discovered: 179062
- Ever alive: 33442
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
