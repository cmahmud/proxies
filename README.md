# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 216
- HTTP: 317 alive / 38 gold
- HTTPS: 203 alive / 10 gold
- SOCKS4: 266 alive / 97 gold
- SOCKS5: 217 alive / 71 gold

## Historical pool

- Discovered: 85902
- Ever alive: 5723
- Ever gold: 288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
