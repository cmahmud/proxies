# SyndProxy private pool

## Current pool

- Alive now: 925
- Gold now: 384
- HTTP: 301 alive / 81 gold
- HTTPS: 195 alive / 21 gold
- SOCKS4: 214 alive / 145 gold
- SOCKS5: 215 alive / 137 gold

## Historical pool

- Discovered: 144770
- Ever alive: 25312
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
