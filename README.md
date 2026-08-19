# SyndProxy private pool

## Current pool

- Alive now: 1304
- Gold now: 385
- HTTP: 441 alive / 88 gold
- HTTPS: 294 alive / 21 gold
- SOCKS4: 258 alive / 138 gold
- SOCKS5: 311 alive / 138 gold

## Historical pool

- Discovered: 133938
- Ever alive: 21517
- Ever gold: 884

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
