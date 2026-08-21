# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 432
- HTTP: 306 alive / 91 gold
- HTTPS: 221 alive / 30 gold
- SOCKS4: 211 alive / 154 gold
- SOCKS5: 249 alive / 157 gold

## Historical pool

- Discovered: 159260
- Ever alive: 30237
- Ever gold: 1144

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
