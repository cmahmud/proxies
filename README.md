# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 366
- HTTP: 87 alive / 45 gold
- HTTPS: 39 alive / 10 gold
- SOCKS4: 184 alive / 155 gold
- SOCKS5: 192 alive / 156 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32993
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
