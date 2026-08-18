# SyndProxy private pool

## Current pool

- Alive now: 960
- Gold now: 345
- HTTP: 300 alive / 56 gold
- HTTPS: 208 alive / 14 gold
- SOCKS4: 226 alive / 140 gold
- SOCKS5: 226 alive / 135 gold

## Historical pool

- Discovered: 107138
- Ever alive: 15082
- Ever gold: 479

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
