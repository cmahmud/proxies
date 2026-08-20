# SyndProxy private pool

## Current pool

- Alive now: 1158
- Gold now: 409
- HTTP: 362 alive / 96 gold
- HTTPS: 291 alive / 23 gold
- SOCKS4: 193 alive / 125 gold
- SOCKS5: 312 alive / 165 gold

## Historical pool

- Discovered: 143501
- Ever alive: 24855
- Ever gold: 1051

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
