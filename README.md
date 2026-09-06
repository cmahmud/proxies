# SyndProxy validated proxy pool

## Current pool

- Alive now: 402
- Gold now: 328
- HTTP: 72 alive / 53 gold
- HTTPS: 41 alive / 18 gold
- SOCKS4: 143 alive / 133 gold
- SOCKS5: 146 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48339
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
