# SyndProxy private pool

## Current pool

- Alive now: 883
- Gold now: 329
- HTTP: 278 alive / 60 gold
- HTTPS: 196 alive / 12 gold
- SOCKS4: 214 alive / 141 gold
- SOCKS5: 195 alive / 116 gold

## Historical pool

- Discovered: 109944
- Ever alive: 15198
- Ever gold: 489

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
