# SyndProxy private pool

## Current pool

- Alive now: 1051
- Gold now: 517
- HTTP: 363 alive / 151 gold
- HTTPS: 262 alive / 87 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 207 alive / 132 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17708
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
