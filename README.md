# SyndProxy private pool

## Current pool

- Alive now: 964
- Gold now: 310
- HTTP: 300 alive / 26 gold
- HTTPS: 182 alive / 4 gold
- SOCKS4: 242 alive / 148 gold
- SOCKS5: 240 alive / 132 gold

## Historical pool

- Discovered: 102812
- Ever alive: 12773
- Ever gold: 412

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
