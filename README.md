# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 373
- HTTP: 310 alive / 71 gold
- HTTPS: 202 alive / 20 gold
- SOCKS4: 198 alive / 137 gold
- SOCKS5: 211 alive / 145 gold

## Historical pool

- Discovered: 157406
- Ever alive: 29675
- Ever gold: 1135

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
