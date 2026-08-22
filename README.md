# SyndProxy private pool

## Current pool

- Alive now: 840
- Gold now: 341
- HTTP: 256 alive / 91 gold
- HTTPS: 191 alive / 30 gold
- SOCKS4: 171 alive / 90 gold
- SOCKS5: 222 alive / 130 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32554
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
