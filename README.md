# SyndProxy private pool

## Current pool

- Alive now: 878
- Gold now: 401
- HTTP: 249 alive / 91 gold
- HTTPS: 188 alive / 26 gold
- SOCKS4: 210 alive / 133 gold
- SOCKS5: 231 alive / 151 gold

## Historical pool

- Discovered: 161996
- Ever alive: 31336
- Ever gold: 1157

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
