# SyndProxy private pool

## Current pool

- Alive now: 1230
- Gold now: 392
- HTTP: 400 alive / 91 gold
- HTTPS: 299 alive / 22 gold
- SOCKS4: 223 alive / 128 gold
- SOCKS5: 308 alive / 151 gold

## Historical pool

- Discovered: 134558
- Ever alive: 22143
- Ever gold: 893

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
