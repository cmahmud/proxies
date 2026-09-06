# SyndProxy validated proxy pool

## Current pool

- Alive now: 447
- Gold now: 371
- HTTP: 75 alive / 50 gold
- HTTPS: 30 alive / 13 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 178 alive / 153 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48306
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
