# SyndProxy private pool

## Current pool

- Alive now: 873
- Gold now: 330
- HTTP: 278 alive / 61 gold
- HTTPS: 190 alive / 12 gold
- SOCKS4: 213 alive / 141 gold
- SOCKS5: 192 alive / 116 gold

## Historical pool

- Discovered: 109944
- Ever alive: 15198
- Ever gold: 489

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
