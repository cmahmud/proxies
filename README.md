# SyndProxy private pool

## Current pool

- Alive now: 1170
- Gold now: 563
- HTTP: 422 alive / 187 gold
- HTTPS: 284 alive / 110 gold
- SOCKS4: 227 alive / 122 gold
- SOCKS5: 237 alive / 144 gold

## Historical pool

- Discovered: 124836
- Ever alive: 19282
- Ever gold: 771

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
