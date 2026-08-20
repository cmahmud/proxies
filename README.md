# SyndProxy private pool

## Current pool

- Alive now: 744
- Gold now: 378
- HTTP: 184 alive / 75 gold
- HTTPS: 140 alive / 18 gold
- SOCKS4: 203 alive / 145 gold
- SOCKS5: 217 alive / 140 gold

## Historical pool

- Discovered: 148338
- Ever alive: 26316
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
