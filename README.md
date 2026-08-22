# SyndProxy private pool

## Current pool

- Alive now: 1066
- Gold now: 412
- HTTP: 369 alive / 91 gold
- HTTPS: 213 alive / 26 gold
- SOCKS4: 227 alive / 135 gold
- SOCKS5: 257 alive / 160 gold

## Historical pool

- Discovered: 166609
- Ever alive: 32425
- Ever gold: 1181

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
