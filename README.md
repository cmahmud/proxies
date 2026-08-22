# SyndProxy private pool

## Current pool

- Alive now: 1103
- Gold now: 422
- HTTP: 327 alive / 91 gold
- HTTPS: 226 alive / 25 gold
- SOCKS4: 248 alive / 139 gold
- SOCKS5: 302 alive / 167 gold

## Historical pool

- Discovered: 164947
- Ever alive: 32219
- Ever gold: 1174

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
