# SyndProxy private pool

## Current pool

- Alive now: 921
- Gold now: 216
- HTTP: 308 alive / 38 gold
- HTTPS: 183 alive / 10 gold
- SOCKS4: 229 alive / 97 gold
- SOCKS5: 201 alive / 71 gold

## Historical pool

- Discovered: 85902
- Ever alive: 5723
- Ever gold: 288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
