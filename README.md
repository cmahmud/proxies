# SyndProxy private pool

## Current pool

- Alive now: 727
- Gold now: 237
- HTTP: 237 alive / 38 gold
- HTTPS: 86 alive / 7 gold
- SOCKS4: 201 alive / 124 gold
- SOCKS5: 203 alive / 68 gold

## Historical pool

- Discovered: 94340
- Ever alive: 9442
- Ever gold: 364

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
