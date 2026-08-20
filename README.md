# SyndProxy private pool

## Current pool

- Alive now: 1674
- Gold now: 597
- HTTP: 620 alive / 217 gold
- HTTPS: 490 alive / 106 gold
- SOCKS4: 209 alive / 135 gold
- SOCKS5: 355 alive / 139 gold

## Historical pool

- Discovered: 141215
- Ever alive: 23887
- Ever gold: 962

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
