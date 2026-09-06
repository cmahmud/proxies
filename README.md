# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 390
- HTTP: 94 alive / 61 gold
- HTTPS: 46 alive / 17 gold
- SOCKS4: 179 alive / 157 gold
- SOCKS5: 178 alive / 155 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48157
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
