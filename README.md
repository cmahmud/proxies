# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 365
- HTTP: 83 alive / 43 gold
- HTTPS: 48 alive / 7 gold
- SOCKS4: 176 alive / 156 gold
- SOCKS5: 204 alive / 159 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32999
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
