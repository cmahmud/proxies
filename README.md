# SyndProxy private pool

## Current pool

- Alive now: 1433
- Gold now: 463
- HTTP: 525 alive / 105 gold
- HTTPS: 378 alive / 33 gold
- SOCKS4: 241 alive / 154 gold
- SOCKS5: 289 alive / 171 gold

## Historical pool

- Discovered: 159265
- Ever alive: 30354
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
