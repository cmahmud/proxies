# SyndProxy validated proxy pool

## Current pool

- Alive now: 435
- Gold now: 332
- HTTP: 86 alive / 60 gold
- HTTPS: 43 alive / 17 gold
- SOCKS4: 155 alive / 135 gold
- SOCKS5: 151 alive / 120 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48351
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
