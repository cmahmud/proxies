# SyndProxy private pool

## Current pool

- Alive now: 916
- Gold now: 337
- HTTP: 304 alive / 82 gold
- HTTPS: 218 alive / 25 gold
- SOCKS4: 209 alive / 140 gold
- SOCKS5: 185 alive / 90 gold

## Historical pool

- Discovered: 167096
- Ever alive: 32500
- Ever gold: 1184

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
