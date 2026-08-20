# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 391
- HTTP: 349 alive / 84 gold
- HTTPS: 218 alive / 22 gold
- SOCKS4: 200 alive / 130 gold
- SOCKS5: 232 alive / 155 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24988
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
