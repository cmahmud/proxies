# SyndProxy private pool

## Current pool

- Alive now: 940
- Gold now: 190
- HTTP: 256 alive / 36 gold
- HTTPS: 233 alive / 10 gold
- SOCKS4: 264 alive / 76 gold
- SOCKS5: 187 alive / 68 gold

## Historical pool

- Discovered: 82934
- Ever alive: 5060
- Ever gold: 259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
