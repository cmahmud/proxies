# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 374
- HTTP: 197 alive / 83 gold
- HTTPS: 130 alive / 21 gold
- SOCKS4: 205 alive / 131 gold
- SOCKS5: 212 alive / 139 gold

## Historical pool

- Discovered: 155683
- Ever alive: 29205
- Ever gold: 1124

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
