# SyndProxy private pool

## Current pool

- Alive now: 1088
- Gold now: 389
- HTTP: 359 alive / 86 gold
- HTTPS: 239 alive / 19 gold
- SOCKS4: 233 alive / 147 gold
- SOCKS5: 257 alive / 137 gold

## Historical pool

- Discovered: 158238
- Ever alive: 29995
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
