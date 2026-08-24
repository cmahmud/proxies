# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 381
- HTTP: 101 alive / 55 gold
- HTTPS: 43 alive / 12 gold
- SOCKS4: 169 alive / 156 gold
- SOCKS5: 179 alive / 158 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33457
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
