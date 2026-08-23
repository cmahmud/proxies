# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 369
- HTTP: 73 alive / 45 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 192 alive / 156 gold
- SOCKS5: 192 alive / 157 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32993
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
