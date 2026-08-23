# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 356
- HTTP: 72 alive / 43 gold
- HTTPS: 65 alive / 9 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 199 alive / 148 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32994
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
