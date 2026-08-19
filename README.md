# SyndProxy private pool

## Current pool

- Alive now: 1098
- Gold now: 513
- HTTP: 395 alive / 149 gold
- HTTPS: 278 alive / 88 gold
- SOCKS4: 216 alive / 146 gold
- SOCKS5: 209 alive / 130 gold

## Historical pool

- Discovered: 117170
- Ever alive: 17703
- Ever gold: 692

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
