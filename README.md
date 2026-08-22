# SyndProxy private pool

## Current pool

- Alive now: 982
- Gold now: 380
- HTTP: 327 alive / 84 gold
- HTTPS: 217 alive / 25 gold
- SOCKS4: 212 alive / 125 gold
- SOCKS5: 226 alive / 146 gold

## Historical pool

- Discovered: 163880
- Ever alive: 32041
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
