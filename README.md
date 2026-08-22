# SyndProxy private pool

## Current pool

- Alive now: 896
- Gold now: 449
- HTTP: 266 alive / 100 gold
- HTTPS: 160 alive / 25 gold
- SOCKS4: 218 alive / 159 gold
- SOCKS5: 252 alive / 165 gold

## Historical pool

- Discovered: 167122
- Ever alive: 32541
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
