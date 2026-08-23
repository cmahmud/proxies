# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 359
- HTTP: 81 alive / 45 gold
- HTTPS: 46 alive / 9 gold
- SOCKS4: 177 alive / 156 gold
- SOCKS5: 202 alive / 149 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32995
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
