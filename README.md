# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 367
- HTTP: 82 alive / 46 gold
- HTTPS: 36 alive / 10 gold
- SOCKS4: 176 alive / 155 gold
- SOCKS5: 189 alive / 156 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32993
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
