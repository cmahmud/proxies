# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 393
- HTTP: 114 alive / 55 gold
- HTTPS: 61 alive / 15 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 196 alive / 162 gold

## Historical pool

- Discovered: 179924
- Ever alive: 33530
- Ever gold: 1240

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
