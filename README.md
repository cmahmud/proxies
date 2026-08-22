# SyndProxy private pool

## Current pool

- Alive now: 969
- Gold now: 406
- HTTP: 291 alive / 92 gold
- HTTPS: 228 alive / 33 gold
- SOCKS4: 219 alive / 147 gold
- SOCKS5: 231 alive / 134 gold

## Historical pool

- Discovered: 161987
- Ever alive: 31293
- Ever gold: 1156

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
