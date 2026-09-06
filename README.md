# SyndProxy validated proxy pool

## Current pool

- Alive now: 419
- Gold now: 342
- HTTP: 82 alive / 59 gold
- HTTPS: 30 alive / 12 gold
- SOCKS4: 147 alive / 137 gold
- SOCKS5: 160 alive / 134 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48385
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
