# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 393
- HTTP: 90 alive / 61 gold
- HTTPS: 43 alive / 17 gold
- SOCKS4: 175 alive / 156 gold
- SOCKS5: 180 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48149
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
