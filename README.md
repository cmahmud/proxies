# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 388
- HTTP: 92 alive / 61 gold
- HTTPS: 44 alive / 14 gold
- SOCKS4: 181 alive / 157 gold
- SOCKS5: 182 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48153
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
