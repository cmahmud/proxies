# SyndProxy private pool

## Current pool

- Alive now: 952
- Gold now: 245
- HTTP: 330 alive / 29 gold
- HTTPS: 147 alive / 7 gold
- SOCKS4: 237 alive / 114 gold
- SOCKS5: 238 alive / 95 gold

## Historical pool

- Discovered: 91720
- Ever alive: 9081
- Ever gold: 361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
