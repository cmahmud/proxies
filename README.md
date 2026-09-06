# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 387
- HTTP: 103 alive / 69 gold
- HTTPS: 39 alive / 15 gold
- SOCKS4: 166 alive / 150 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48176
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
