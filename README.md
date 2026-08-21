# SyndProxy private pool

## Current pool

- Alive now: 835
- Gold now: 408
- HTTP: 230 alive / 89 gold
- HTTPS: 156 alive / 25 gold
- SOCKS4: 212 alive / 146 gold
- SOCKS5: 237 alive / 148 gold

## Historical pool

- Discovered: 154723
- Ever alive: 29125
- Ever gold: 1123

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
