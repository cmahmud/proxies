# SyndProxy validated proxy pool

## Current pool

- Alive now: 453
- Gold now: 381
- HTTP: 84 alive / 62 gold
- HTTPS: 33 alive / 17 gold
- SOCKS4: 168 alive / 153 gold
- SOCKS5: 168 alive / 149 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48163
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
