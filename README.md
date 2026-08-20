# SyndProxy private pool

## Current pool

- Alive now: 1411
- Gold now: 596
- HTTP: 560 alive / 193 gold
- HTTPS: 373 alive / 100 gold
- SOCKS4: 220 alive / 137 gold
- SOCKS5: 258 alive / 166 gold

## Historical pool

- Discovered: 138843
- Ever alive: 23112
- Ever gold: 914

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
