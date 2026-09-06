# SyndProxy validated proxy pool

## Current pool

- Alive now: 422
- Gold now: 316
- HTTP: 86 alive / 55 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 148 alive / 133 gold
- SOCKS5: 147 alive / 116 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48350
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
