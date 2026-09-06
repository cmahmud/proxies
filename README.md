# SyndProxy validated proxy pool

## Current pool

- Alive now: 420
- Gold now: 306
- HTTP: 85 alive / 60 gold
- HTTPS: 39 alive / 19 gold
- SOCKS4: 150 alive / 122 gold
- SOCKS5: 146 alive / 105 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48361
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
