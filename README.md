# SyndProxy private pool

## Current pool

- Alive now: 1140
- Gold now: 476
- HTTP: 393 alive / 119 gold
- HTTPS: 272 alive / 74 gold
- SOCKS4: 237 alive / 141 gold
- SOCKS5: 238 alive / 142 gold

## Historical pool

- Discovered: 113533
- Ever alive: 16429
- Ever gold: 619

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
