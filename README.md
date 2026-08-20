# SyndProxy private pool

## Current pool

- Alive now: 1308
- Gold now: 563
- HTTP: 493 alive / 189 gold
- HTTPS: 373 alive / 94 gold
- SOCKS4: 217 alive / 146 gold
- SOCKS5: 225 alive / 134 gold

## Historical pool

- Discovered: 138813
- Ever alive: 22944
- Ever gold: 910

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
