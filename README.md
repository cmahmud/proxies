# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 393
- HTTP: 349 alive / 82 gold
- HTTPS: 237 alive / 23 gold
- SOCKS4: 201 alive / 133 gold
- SOCKS5: 253 alive / 155 gold

## Historical pool

- Discovered: 144732
- Ever alive: 24976
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
