# SyndProxy private pool

## Current pool

- Alive now: 1354
- Gold now: 444
- HTTP: 531 alive / 107 gold
- HTTPS: 351 alive / 32 gold
- SOCKS4: 214 alive / 140 gold
- SOCKS5: 258 alive / 165 gold

## Historical pool

- Discovered: 159270
- Ever alive: 30387
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
