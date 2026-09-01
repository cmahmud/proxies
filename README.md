# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 453
- HTTP: 131 alive / 83 gold
- HTTPS: 103 alive / 35 gold
- SOCKS4: 178 alive / 162 gold
- SOCKS5: 189 alive / 173 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46991
- Ever gold: 1462

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
