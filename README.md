# SyndProxy private pool

## Current pool

- Alive now: 1029
- Gold now: 420
- HTTP: 316 alive / 95 gold
- HTTPS: 243 alive / 24 gold
- SOCKS4: 209 alive / 141 gold
- SOCKS5: 261 alive / 160 gold

## Historical pool

- Discovered: 158911
- Ever alive: 30118
- Ever gold: 1140

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
