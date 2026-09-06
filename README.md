# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 390
- HTTP: 98 alive / 68 gold
- HTTPS: 46 alive / 13 gold
- SOCKS4: 173 alive / 153 gold
- SOCKS5: 182 alive / 156 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48105
- Ever gold: 1519

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
