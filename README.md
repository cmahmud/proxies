# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 457
- HTTP: 134 alive / 85 gold
- HTTPS: 103 alive / 36 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 188 alive / 174 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46992
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
