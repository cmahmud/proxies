# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 394
- HTTP: 86 alive / 64 gold
- HTTPS: 43 alive / 16 gold
- SOCKS4: 179 alive / 157 gold
- SOCKS5: 175 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48155
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
