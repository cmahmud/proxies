# SyndProxy private pool

## Current pool

- Alive now: 984
- Gold now: 340
- HTTP: 345 alive / 86 gold
- HTTPS: 244 alive / 24 gold
- SOCKS4: 203 alive / 140 gold
- SOCKS5: 192 alive / 90 gold

## Historical pool

- Discovered: 166948
- Ever alive: 32487
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
