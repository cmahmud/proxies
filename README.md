# SyndProxy validated proxy pool

## Current pool

- Alive now: 418
- Gold now: 329
- HTTP: 86 alive / 63 gold
- HTTPS: 41 alive / 14 gold
- SOCKS4: 144 alive / 133 gold
- SOCKS5: 147 alive / 119 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48363
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
