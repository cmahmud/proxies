# SyndProxy validated proxy pool

## Current pool

- Alive now: 409
- Gold now: 330
- HTTP: 82 alive / 60 gold
- HTTPS: 35 alive / 9 gold
- SOCKS4: 146 alive / 136 gold
- SOCKS5: 146 alive / 125 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48373
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
