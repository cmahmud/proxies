# SyndProxy private pool

## Current pool

- Alive now: 1358
- Gold now: 400
- HTTP: 467 alive / 91 gold
- HTTPS: 299 alive / 17 gold
- SOCKS4: 258 alive / 146 gold
- SOCKS5: 334 alive / 146 gold

## Historical pool

- Discovered: 133966
- Ever alive: 21672
- Ever gold: 887

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
