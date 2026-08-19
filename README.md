# SyndProxy private pool

## Current pool

- Alive now: 1171
- Gold now: 390
- HTTP: 387 alive / 84 gold
- HTTPS: 266 alive / 20 gold
- SOCKS4: 222 alive / 136 gold
- SOCKS5: 296 alive / 150 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22160
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
