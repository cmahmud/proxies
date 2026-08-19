# SyndProxy private pool

## Current pool

- Alive now: 968
- Gold now: 341
- HTTP: 317 alive / 66 gold
- HTTPS: 196 alive / 14 gold
- SOCKS4: 252 alive / 140 gold
- SOCKS5: 203 alive / 121 gold

## Historical pool

- Discovered: 109955
- Ever alive: 15350
- Ever gold: 495

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
