# SyndProxy private pool

## Current pool

- Alive now: 1546
- Gold now: 573
- HTTP: 555 alive / 196 gold
- HTTPS: 400 alive / 96 gold
- SOCKS4: 227 alive / 148 gold
- SOCKS5: 364 alive / 133 gold

## Historical pool

- Discovered: 140465
- Ever alive: 23646
- Ever gold: 924

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
