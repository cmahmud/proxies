# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 228
- HTTP: 287 alive / 29 gold
- HTTPS: 153 alive / 8 gold
- SOCKS4: 240 alive / 110 gold
- SOCKS5: 216 alive / 81 gold

## Historical pool

- Discovered: 86746
- Ever alive: 7591
- Ever gold: 337

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
