# SyndProxy private pool

## Current pool

- Alive now: 1363
- Gold now: 376
- HTTP: 470 alive / 89 gold
- HTTPS: 306 alive / 20 gold
- SOCKS4: 256 alive / 126 gold
- SOCKS5: 331 alive / 141 gold

## Historical pool

- Discovered: 134551
- Ever alive: 22035
- Ever gold: 890

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
