# SyndProxy private pool

## Current pool

- Alive now: 1179
- Gold now: 215
- HTTP: 419 alive / 30 gold
- HTTPS: 230 alive / 10 gold
- SOCKS4: 314 alive / 100 gold
- SOCKS5: 216 alive / 75 gold

## Historical pool

- Discovered: 86675
- Ever alive: 6452
- Ever gold: 295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
