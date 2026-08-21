# SyndProxy private pool

## Current pool

- Alive now: 1213
- Gold now: 441
- HTTP: 431 alive / 108 gold
- HTTPS: 315 alive / 33 gold
- SOCKS4: 210 alive / 153 gold
- SOCKS5: 257 alive / 147 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28626
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
