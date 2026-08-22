# SyndProxy private pool

## Current pool

- Alive now: 845
- Gold now: 360
- HTTP: 252 alive / 89 gold
- HTTPS: 163 alive / 28 gold
- SOCKS4: 193 alive / 104 gold
- SOCKS5: 237 alive / 139 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32556
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
