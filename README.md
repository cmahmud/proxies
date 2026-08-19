# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 395
- HTTP: 396 alive / 92 gold
- HTTPS: 301 alive / 21 gold
- SOCKS4: 218 alive / 130 gold
- SOCKS5: 301 alive / 152 gold

## Historical pool

- Discovered: 134557
- Ever alive: 22140
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
