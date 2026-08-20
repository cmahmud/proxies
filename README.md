# SyndProxy private pool

## Current pool

- Alive now: 1276
- Gold now: 402
- HTTP: 463 alive / 103 gold
- HTTPS: 323 alive / 27 gold
- SOCKS4: 236 alive / 134 gold
- SOCKS5: 254 alive / 138 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25127
- Ever gold: 1055

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
