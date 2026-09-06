# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 394
- HTTP: 125 alive / 81 gold
- HTTPS: 59 alive / 22 gold
- SOCKS4: 157 alive / 138 gold
- SOCKS5: 182 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48032
- Ever gold: 1513

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
