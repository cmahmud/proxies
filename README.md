# SyndProxy private pool

## Current pool

- Alive now: 862
- Gold now: 381
- HTTP: 254 alive / 82 gold
- HTTPS: 157 alive / 23 gold
- SOCKS4: 220 alive / 137 gold
- SOCKS5: 231 alive / 139 gold

## Historical pool

- Discovered: 155799
- Ever alive: 29360
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
