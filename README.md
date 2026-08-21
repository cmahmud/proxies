# SyndProxy private pool

## Current pool

- Alive now: 905
- Gold now: 401
- HTTP: 291 alive / 102 gold
- HTTPS: 209 alive / 31 gold
- SOCKS4: 200 alive / 147 gold
- SOCKS5: 205 alive / 121 gold

## Historical pool

- Discovered: 153184
- Ever alive: 28467
- Ever gold: 1108

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
