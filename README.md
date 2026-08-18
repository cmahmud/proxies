# SyndProxy private pool

## Current pool

- Alive now: 1200
- Gold now: 215
- HTTP: 426 alive / 30 gold
- HTTPS: 230 alive / 10 gold
- SOCKS4: 320 alive / 100 gold
- SOCKS5: 224 alive / 75 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
