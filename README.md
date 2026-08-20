# SyndProxy private pool

## Current pool

- Alive now: 747
- Gold now: 390
- HTTP: 200 alive / 79 gold
- HTTPS: 119 alive / 23 gold
- SOCKS4: 220 alive / 143 gold
- SOCKS5: 208 alive / 145 gold

## Historical pool

- Discovered: 144750
- Ever alive: 25255
- Ever gold: 1057

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
