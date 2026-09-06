# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 387
- HTTP: 87 alive / 61 gold
- HTTPS: 38 alive / 14 gold
- SOCKS4: 184 alive / 157 gold
- SOCKS5: 177 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48153
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
