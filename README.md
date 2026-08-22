# SyndProxy private pool

## Current pool

- Alive now: 794
- Gold now: 339
- HTTP: 251 alive / 94 gold
- HTTPS: 170 alive / 28 gold
- SOCKS4: 152 alive / 88 gold
- SOCKS5: 221 alive / 129 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32552
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
