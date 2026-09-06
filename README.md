# SyndProxy validated proxy pool

## Current pool

- Alive now: 407
- Gold now: 339
- HTTP: 76 alive / 60 gold
- HTTPS: 24 alive / 11 gold
- SOCKS4: 147 alive / 136 gold
- SOCKS5: 160 alive / 132 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48385
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
