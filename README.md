# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 382
- HTTP: 89 alive / 62 gold
- HTTPS: 41 alive / 14 gold
- SOCKS4: 180 alive / 154 gold
- SOCKS5: 181 alive / 152 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48124
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
