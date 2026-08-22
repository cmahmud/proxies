# SyndProxy private pool

## Current pool

- Alive now: 1085
- Gold now: 425
- HTTP: 383 alive / 101 gold
- HTTPS: 279 alive / 32 gold
- SOCKS4: 192 alive / 136 gold
- SOCKS5: 231 alive / 156 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31094
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
