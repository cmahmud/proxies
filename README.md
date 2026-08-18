# SyndProxy private pool

## Current pool

- Alive now: 954
- Gold now: 300
- HTTP: 288 alive / 24 gold
- HTTPS: 182 alive / 4 gold
- SOCKS4: 244 alive / 148 gold
- SOCKS5: 240 alive / 124 gold

## Historical pool

- Discovered: 102812
- Ever alive: 12773
- Ever gold: 404

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
