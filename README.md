# SyndProxy private pool

## Current pool

- Alive now: 632
- Gold now: 241
- HTTP: 160 alive / 31 gold
- HTTPS: 78 alive / 8 gold
- SOCKS4: 196 alive / 114 gold
- SOCKS5: 198 alive / 88 gold

## Historical pool

- Discovered: 86775
- Ever alive: 7595
- Ever gold: 338

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
