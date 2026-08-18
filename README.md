# SyndProxy private pool

## Current pool

- Alive now: 938
- Gold now: 323
- HTTP: 289 alive / 37 gold
- HTTPS: 193 alive / 9 gold
- SOCKS4: 230 alive / 146 gold
- SOCKS5: 226 alive / 131 gold

## Historical pool

- Discovered: 106999
- Ever alive: 14205
- Ever gold: 435

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
