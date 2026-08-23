# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 370
- HTTP: 74 alive / 46 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 196 alive / 156 gold
- SOCKS5: 197 alive / 157 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32993
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
