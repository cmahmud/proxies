# SyndProxy validated proxy pool

## Current pool

- Alive now: 426
- Gold now: 337
- HTTP: 89 alive / 61 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 148 alive / 137 gold
- SOCKS5: 151 alive / 124 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48377
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
