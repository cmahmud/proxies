# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 415
- HTTP: 101 alive / 67 gold
- HTTPS: 70 alive / 23 gold
- SOCKS4: 174 alive / 158 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47037
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
