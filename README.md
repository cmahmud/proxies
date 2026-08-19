# SyndProxy private pool

## Current pool

- Alive now: 1053
- Gold now: 369
- HTTP: 362 alive / 78 gold
- HTTPS: 252 alive / 11 gold
- SOCKS4: 214 alive / 127 gold
- SOCKS5: 225 alive / 153 gold

## Historical pool

- Discovered: 129304
- Ever alive: 20384
- Ever gold: 865

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
