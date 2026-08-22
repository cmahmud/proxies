# SyndProxy private pool

## Current pool

- Alive now: 783
- Gold now: 338
- HTTP: 253 alive / 97 gold
- HTTPS: 149 alive / 26 gold
- SOCKS4: 160 alive / 85 gold
- SOCKS5: 221 alive / 130 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32552
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
