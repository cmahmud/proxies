# SyndProxy private pool

## Current pool

- Alive now: 1042
- Gold now: 534
- HTTP: 377 alive / 154 gold
- HTTPS: 232 alive / 88 gold
- SOCKS4: 220 alive / 149 gold
- SOCKS5: 213 alive / 143 gold

## Historical pool

- Discovered: 119812
- Ever alive: 18040
- Ever gold: 713

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
