# SyndProxy private pool

## Current pool

- Alive now: 951
- Gold now: 319
- HTTP: 287 alive / 39 gold
- HTTPS: 199 alive / 10 gold
- SOCKS4: 242 alive / 137 gold
- SOCKS5: 223 alive / 133 gold

## Historical pool

- Discovered: 107013
- Ever alive: 14260
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
