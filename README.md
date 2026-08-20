# SyndProxy private pool

## Current pool

- Alive now: 726
- Gold now: 371
- HTTP: 156 alive / 71 gold
- HTTPS: 143 alive / 17 gold
- SOCKS4: 226 alive / 146 gold
- SOCKS5: 201 alive / 137 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26264
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
