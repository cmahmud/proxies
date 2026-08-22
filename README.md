# SyndProxy private pool

## Current pool

- Alive now: 998
- Gold now: 395
- HTTP: 339 alive / 90 gold
- HTTPS: 220 alive / 26 gold
- SOCKS4: 183 alive / 114 gold
- SOCKS5: 256 alive / 165 gold

## Historical pool

- Discovered: 166621
- Ever alive: 32451
- Ever gold: 1183

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
