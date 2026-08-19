# SyndProxy private pool

## Current pool

- Alive now: 908
- Gold now: 463
- HTTP: 293 alive / 117 gold
- HTTPS: 204 alive / 87 gold
- SOCKS4: 217 alive / 141 gold
- SOCKS5: 194 alive / 118 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17488
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
