# SyndProxy private pool

## Current pool

- Alive now: 1021
- Gold now: 466
- HTTP: 367 alive / 126 gold
- HTTPS: 258 alive / 86 gold
- SOCKS4: 218 alive / 143 gold
- SOCKS5: 178 alive / 111 gold

## Historical pool

- Discovered: 117130
- Ever alive: 17463
- Ever gold: 664

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
