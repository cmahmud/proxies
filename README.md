# SyndProxy private pool

## Current pool

- Alive now: 1844
- Gold now: 619
- HTTP: 801 alive / 240 gold
- HTTPS: 608 alive / 114 gold
- SOCKS4: 182 alive / 103 gold
- SOCKS5: 253 alive / 162 gold

## Historical pool

- Discovered: 143486
- Ever alive: 24773
- Ever gold: 1038

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
