# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 390
- HTTP: 92 alive / 61 gold
- HTTPS: 37 alive / 16 gold
- SOCKS4: 178 alive / 157 gold
- SOCKS5: 179 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48160
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
