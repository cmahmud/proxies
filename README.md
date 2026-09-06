# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 394
- HTTP: 125 alive / 79 gold
- HTTPS: 57 alive / 23 gold
- SOCKS4: 156 alive / 138 gold
- SOCKS5: 185 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48030
- Ever gold: 1513

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
