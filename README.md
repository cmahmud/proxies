# SyndProxy private pool

## Current pool

- Alive now: 1184
- Gold now: 402
- HTTP: 422 alive / 103 gold
- HTTPS: 284 alive / 29 gold
- SOCKS4: 204 alive / 118 gold
- SOCKS5: 274 alive / 152 gold

## Historical pool

- Discovered: 152758
- Ever alive: 28336
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
