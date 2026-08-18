# SyndProxy private pool

## Current pool

- Alive now: 826
- Gold now: 190
- HTTP: 255 alive / 36 gold
- HTTPS: 148 alive / 10 gold
- SOCKS4: 246 alive / 76 gold
- SOCKS5: 177 alive / 68 gold

## Historical pool

- Discovered: 82934
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
