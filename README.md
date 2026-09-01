# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 414
- HTTP: 101 alive / 66 gold
- HTTPS: 75 alive / 23 gold
- SOCKS4: 170 alive / 158 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47037
- Ever gold: 1463

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
