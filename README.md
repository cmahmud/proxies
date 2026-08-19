# SyndProxy private pool

## Current pool

- Alive now: 1058
- Gold now: 369
- HTTP: 366 alive / 76 gold
- HTTPS: 250 alive / 11 gold
- SOCKS4: 217 alive / 128 gold
- SOCKS5: 225 alive / 154 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20384
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
