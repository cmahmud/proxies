# SyndProxy private pool

## Current pool

- Alive now: 1034
- Gold now: 334
- HTTP: 360 alive / 64 gold
- HTTPS: 210 alive / 8 gold
- SOCKS4: 248 alive / 141 gold
- SOCKS5: 216 alive / 121 gold

## Historical pool

- Discovered: 129271
- Ever alive: 20252
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
