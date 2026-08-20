# SyndProxy private pool

## Current pool

- Alive now: 1007
- Gold now: 397
- HTTP: 313 alive / 86 gold
- HTTPS: 209 alive / 24 gold
- SOCKS4: 199 alive / 132 gold
- SOCKS5: 286 alive / 155 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25011
- Ever gold: 1053

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
