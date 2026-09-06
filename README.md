# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 391
- HTTP: 91 alive / 62 gold
- HTTPS: 42 alive / 15 gold
- SOCKS4: 177 alive / 157 gold
- SOCKS5: 177 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48156
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
