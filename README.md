# SyndProxy private pool

## Current pool

- Alive now: 1000
- Gold now: 354
- HTTP: 326 alive / 56 gold
- HTTPS: 201 alive / 14 gold
- SOCKS4: 243 alive / 147 gold
- SOCKS5: 230 alive / 137 gold

## Historical pool

- Discovered: 107154
- Ever alive: 15128
- Ever gold: 483

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
