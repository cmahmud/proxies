# SyndProxy private pool

## Current pool

- Alive now: 986
- Gold now: 245
- HTTP: 376 alive / 28 gold
- HTTPS: 189 alive / 1 gold
- SOCKS4: 203 alive / 122 gold
- SOCKS5: 218 alive / 94 gold

## Historical pool

- Discovered: 95391
- Ever alive: 10585
- Ever gold: 377

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
