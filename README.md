# SyndProxy private pool

## Current pool

- Alive now: 1009
- Gold now: 415
- HTTP: 327 alive / 89 gold
- HTTPS: 203 alive / 24 gold
- SOCKS4: 216 alive / 146 gold
- SOCKS5: 263 alive / 156 gold

## Historical pool

- Discovered: 156426
- Ever alive: 29515
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
