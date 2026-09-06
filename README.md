# SyndProxy validated proxy pool

## Current pool

- Alive now: 410
- Gold now: 334
- HTTP: 79 alive / 56 gold
- HTTPS: 38 alive / 18 gold
- SOCKS4: 143 alive / 134 gold
- SOCKS5: 150 alive / 126 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48342
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
