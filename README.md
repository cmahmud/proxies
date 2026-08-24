# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 386
- HTTP: 102 alive / 57 gold
- HTTPS: 49 alive / 14 gold
- SOCKS4: 170 alive / 156 gold
- SOCKS5: 179 alive / 159 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33457
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
