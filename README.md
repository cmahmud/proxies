# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 367
- HTTP: 92 alive / 45 gold
- HTTPS: 41 alive / 10 gold
- SOCKS4: 178 alive / 155 gold
- SOCKS5: 208 alive / 157 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32993
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
