# SyndProxy private pool

## Current pool

- Alive now: 802
- Gold now: 362
- HTTP: 222 alive / 89 gold
- HTTPS: 157 alive / 30 gold
- SOCKS4: 186 alive / 104 gold
- SOCKS5: 237 alive / 139 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32555
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
