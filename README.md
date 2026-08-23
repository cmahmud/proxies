# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 363
- HTTP: 80 alive / 43 gold
- HTTPS: 48 alive / 7 gold
- SOCKS4: 175 alive / 155 gold
- SOCKS5: 201 alive / 158 gold

## Historical pool

- Discovered: 173052
- Ever alive: 32999
- Ever gold: 1222

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
