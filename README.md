# SyndProxy private pool

## Current pool

- Alive now: 1044
- Gold now: 425
- HTTP: 291 alive / 93 gold
- HTTPS: 204 alive / 24 gold
- SOCKS4: 237 alive / 139 gold
- SOCKS5: 312 alive / 169 gold

## Historical pool

- Discovered: 164947
- Ever alive: 32218
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
