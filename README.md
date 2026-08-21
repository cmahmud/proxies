# SyndProxy private pool

## Current pool

- Alive now: 1013
- Gold now: 424
- HTTP: 346 alive / 88 gold
- HTTPS: 222 alive / 28 gold
- SOCKS4: 216 alive / 150 gold
- SOCKS5: 229 alive / 158 gold

## Historical pool

- Discovered: 156424
- Ever alive: 29494
- Ever gold: 1129

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
