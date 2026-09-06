# SyndProxy validated proxy pool

## Current pool

- Alive now: 427
- Gold now: 330
- HTTP: 84 alive / 57 gold
- HTTPS: 31 alive / 10 gold
- SOCKS4: 150 alive / 135 gold
- SOCKS5: 162 alive / 128 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48392
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
