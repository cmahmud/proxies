# SyndProxy private pool

## Current pool

- Alive now: 1464
- Gold now: 505
- HTTP: 553 alive / 151 gold
- HTTPS: 335 alive / 62 gold
- SOCKS4: 241 alive / 136 gold
- SOCKS5: 335 alive / 156 gold

## Historical pool

- Discovered: 136248
- Ever alive: 22695
- Ever gold: 909

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
