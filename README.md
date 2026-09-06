# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 391
- HTTP: 92 alive / 68 gold
- HTTPS: 40 alive / 14 gold
- SOCKS4: 174 alive / 152 gold
- SOCKS5: 178 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48116
- Ever gold: 1520

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
