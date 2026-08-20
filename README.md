# SyndProxy private pool

## Current pool

- Alive now: 1037
- Gold now: 400
- HTTP: 346 alive / 88 gold
- HTTPS: 207 alive / 24 gold
- SOCKS4: 207 alive / 132 gold
- SOCKS5: 277 alive / 156 gold

## Historical pool

- Discovered: 144740
- Ever alive: 24998
- Ever gold: 1053

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
