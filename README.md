# SyndProxy validated proxy pool

## Current pool

- Alive now: 635
- Gold now: 300
- HTTP: 163 alive / 74 gold
- HTTPS: 39 alive / 23 gold
- SOCKS4: 231 alive / 68 gold
- SOCKS5: 202 alive / 135 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47802
- Ever gold: 1470

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
