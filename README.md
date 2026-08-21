# SyndProxy private pool

## Current pool

- Alive now: 1083
- Gold now: 433
- HTTP: 371 alive / 103 gold
- HTTPS: 241 alive / 29 gold
- SOCKS4: 206 alive / 141 gold
- SOCKS5: 265 alive / 160 gold

## Historical pool

- Discovered: 153726
- Ever alive: 28659
- Ever gold: 1110

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
