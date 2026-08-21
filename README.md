# SyndProxy private pool

## Current pool

- Alive now: 1235
- Gold now: 417
- HTTP: 433 alive / 109 gold
- HTTPS: 329 alive / 29 gold
- SOCKS4: 234 alive / 152 gold
- SOCKS5: 239 alive / 127 gold

## Historical pool

- Discovered: 159262
- Ever alive: 30331
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
