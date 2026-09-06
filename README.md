# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 392
- HTTP: 95 alive / 60 gold
- HTTPS: 39 alive / 18 gold
- SOCKS4: 179 alive / 157 gold
- SOCKS5: 179 alive / 157 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48160
- Ever gold: 1521

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
