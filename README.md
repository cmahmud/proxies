# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 365
- HTTP: 131 alive / 79 gold
- HTTPS: 66 alive / 24 gold
- SOCKS4: 140 alive / 116 gold
- SOCKS5: 177 alive / 146 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47996
- Ever gold: 1508

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
