# SyndProxy private pool

## Current pool

- Alive now: 669
- Gold now: 383
- HTTP: 167 alive / 69 gold
- HTTPS: 86 alive / 14 gold
- SOCKS4: 198 alive / 140 gold
- SOCKS5: 218 alive / 160 gold

## Historical pool

- Discovered: 147177
- Ever alive: 25790
- Ever gold: 1076

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
