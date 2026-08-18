# SyndProxy private pool

## Current pool

- Alive now: 823
- Gold now: 263
- HTTP: 223 alive / 32 gold
- HTTPS: 157 alive / 5 gold
- SOCKS4: 201 alive / 120 gold
- SOCKS5: 242 alive / 106 gold

## Historical pool

- Discovered: 98220
- Ever alive: 11096
- Ever gold: 382

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
