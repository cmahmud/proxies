# SyndProxy private pool

## Current pool

- Alive now: 739
- Gold now: 382
- HTTP: 244 alive / 67 gold
- HTTPS: 101 alive / 19 gold
- SOCKS4: 186 alive / 149 gold
- SOCKS5: 208 alive / 147 gold

## Historical pool

- Discovered: 146664
- Ever alive: 25747
- Ever gold: 1074

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
