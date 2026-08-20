# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 381
- HTTP: 274 alive / 93 gold
- HTTPS: 212 alive / 28 gold
- SOCKS4: 212 alive / 129 gold
- SOCKS5: 240 alive / 131 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25058
- Ever gold: 1054

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
