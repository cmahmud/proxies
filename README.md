# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 370
- HTTP: 74 alive / 47 gold
- HTTPS: 64 alive / 11 gold
- SOCKS4: 188 alive / 156 gold
- SOCKS5: 195 alive / 156 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32994
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
