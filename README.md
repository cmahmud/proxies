# SyndProxy private pool

## Current pool

- Alive now: 837
- Gold now: 340
- HTTP: 265 alive / 98 gold
- HTTPS: 168 alive / 26 gold
- SOCKS4: 171 alive / 86 gold
- SOCKS5: 233 alive / 130 gold

## Historical pool

- Discovered: 167354
- Ever alive: 32553
- Ever gold: 1188

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
