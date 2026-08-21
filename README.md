# SyndProxy private pool

## Current pool

- Alive now: 1260
- Gold now: 428
- HTTP: 493 alive / 95 gold
- HTTPS: 320 alive / 30 gold
- SOCKS4: 203 alive / 140 gold
- SOCKS5: 244 alive / 163 gold

## Historical pool

- Discovered: 159270
- Ever alive: 30388
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
