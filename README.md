# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 382
- HTTP: 106 alive / 55 gold
- HTTPS: 41 alive / 13 gold
- SOCKS4: 167 alive / 156 gold
- SOCKS5: 178 alive / 158 gold

## Historical pool

- Discovered: 179370
- Ever alive: 33457
- Ever gold: 1238

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
