# SyndProxy validated proxy pool

## Current pool

- Alive now: 590
- Gold now: 433
- HTTP: 121 alive / 74 gold
- HTTPS: 98 alive / 23 gold
- SOCKS4: 179 alive / 165 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47601
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
