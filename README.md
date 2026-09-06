# SyndProxy validated proxy pool

## Current pool

- Alive now: 464
- Gold now: 379
- HTTP: 89 alive / 59 gold
- HTTPS: 36 alive / 17 gold
- SOCKS4: 170 alive / 153 gold
- SOCKS5: 169 alive / 150 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48163
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
