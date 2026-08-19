# SyndProxy private pool

## Current pool

- Alive now: 983
- Gold now: 422
- HTTP: 294 alive / 91 gold
- HTTPS: 193 alive / 21 gold
- SOCKS4: 226 alive / 148 gold
- SOCKS5: 270 alive / 162 gold

## Historical pool

- Discovered: 136206
- Ever alive: 22330
- Ever gold: 896

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
