# SyndProxy private pool

## Current pool

- Alive now: 748
- Gold now: 412
- HTTP: 209 alive / 89 gold
- HTTPS: 126 alive / 20 gold
- SOCKS4: 201 alive / 147 gold
- SOCKS5: 212 alive / 156 gold

## Historical pool

- Discovered: 152160
- Ever alive: 27835
- Ever gold: 1103

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
