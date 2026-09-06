# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 394
- HTTP: 90 alive / 62 gold
- HTTPS: 43 alive / 17 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 181 alive / 159 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48150
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
