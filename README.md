# SyndProxy private pool

## Current pool

- Alive now: 1197
- Gold now: 398
- HTTP: 434 alive / 97 gold
- HTTPS: 318 alive / 28 gold
- SOCKS4: 231 alive / 152 gold
- SOCKS5: 214 alive / 121 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30317
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
