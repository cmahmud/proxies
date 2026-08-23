# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 363
- HTTP: 103 alive / 37 gold
- HTTPS: 48 alive / 10 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 185 alive / 156 gold

## Historical pool

- Discovered: 171584
- Ever alive: 32926
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
