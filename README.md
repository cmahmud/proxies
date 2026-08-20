# SyndProxy private pool

## Current pool

- Alive now: 1008
- Gold now: 388
- HTTP: 342 alive / 83 gold
- HTTPS: 236 alive / 20 gold
- SOCKS4: 198 alive / 130 gold
- SOCKS5: 232 alive / 155 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24978
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
