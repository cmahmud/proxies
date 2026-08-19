# SyndProxy private pool

## Current pool

- Alive now: 1047
- Gold now: 369
- HTTP: 350 alive / 76 gold
- HTTPS: 255 alive / 11 gold
- SOCKS4: 215 alive / 128 gold
- SOCKS5: 227 alive / 154 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20377
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
