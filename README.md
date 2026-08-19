# SyndProxy private pool

## Current pool

- Alive now: 913
- Gold now: 327
- HTTP: 272 alive / 55 gold
- HTTPS: 191 alive / 9 gold
- SOCKS4: 231 alive / 138 gold
- SOCKS5: 219 alive / 125 gold

## Historical pool

- Discovered: 129285
- Ever alive: 20264
- Ever gold: 864

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
