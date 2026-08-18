# SyndProxy private pool

## Current pool

- Alive now: 648
- Gold now: 214
- HTTP: 183 alive / 28 gold
- HTTPS: 90 alive / 8 gold
- SOCKS4: 195 alive / 102 gold
- SOCKS5: 180 alive / 76 gold

## Historical pool

- Discovered: 86694
- Ever alive: 6452
- Ever gold: 296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
