# SyndProxy private pool

## Current pool

- Alive now: 981
- Gold now: 355
- HTTP: 313 alive / 68 gold
- HTTPS: 213 alive / 12 gold
- SOCKS4: 208 alive / 129 gold
- SOCKS5: 247 alive / 146 gold

## Historical pool

- Discovered: 129290
- Ever alive: 20342
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
