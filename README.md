# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 412
- HTTP: 102 alive / 65 gold
- HTTPS: 145 alive / 17 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 190445
- Ever alive: 41231
- Ever gold: 1319

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
