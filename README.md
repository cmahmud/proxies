# SyndProxy validated proxy pool

## Current pool

- Alive now: 412
- Gold now: 339
- HTTP: 79 alive / 60 gold
- HTTPS: 29 alive / 13 gold
- SOCKS4: 146 alive / 135 gold
- SOCKS5: 158 alive / 131 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48389
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
