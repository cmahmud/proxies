# SyndProxy validated proxy pool

## Current pool

- Alive now: 591
- Gold now: 435
- HTTP: 120 alive / 75 gold
- HTTPS: 101 alive / 24 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 191 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47601
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
