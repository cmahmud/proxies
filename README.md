# SyndProxy validated proxy pool

## Current pool

- Alive now: 403
- Gold now: 341
- HTTP: 74 alive / 62 gold
- HTTPS: 23 alive / 9 gold
- SOCKS4: 145 alive / 137 gold
- SOCKS5: 161 alive / 133 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48386
- Ever gold: 1530

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
