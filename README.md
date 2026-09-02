# SyndProxy validated proxy pool

## Current pool

- Alive now: 601
- Gold now: 443
- HTTP: 103 alive / 78 gold
- HTTPS: 121 alive / 27 gold
- SOCKS4: 180 alive / 161 gold
- SOCKS5: 197 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47557
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
