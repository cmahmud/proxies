# SyndProxy validated proxy pool

## Current pool

- Alive now: 446
- Gold now: 343
- HTTP: 92 alive / 55 gold
- HTTPS: 35 alive / 10 gold
- SOCKS4: 149 alive / 140 gold
- SOCKS5: 170 alive / 138 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48400
- Ever gold: 1531

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
