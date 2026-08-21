# SyndProxy private pool

## Current pool

- Alive now: 1255
- Gold now: 412
- HTTP: 434 alive / 107 gold
- HTTPS: 333 alive / 28 gold
- SOCKS4: 246 alive / 151 gold
- SOCKS5: 242 alive / 126 gold

## Historical pool

- Discovered: 159262
- Ever alive: 30332
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
