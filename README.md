# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 358
- HTTP: 73 alive / 43 gold
- HTTPS: 70 alive / 10 gold
- SOCKS4: 184 alive / 156 gold
- SOCKS5: 195 alive / 149 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32994
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
