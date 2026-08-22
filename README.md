# SyndProxy private pool

## Current pool

- Alive now: 995
- Gold now: 401
- HTTP: 308 alive / 81 gold
- HTTPS: 224 alive / 29 gold
- SOCKS4: 212 alive / 126 gold
- SOCKS5: 251 alive / 165 gold

## Historical pool

- Discovered: 164960
- Ever alive: 32241
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
