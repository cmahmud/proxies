# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 397
- HTTP: 335 alive / 87 gold
- HTTPS: 212 alive / 23 gold
- SOCKS4: 201 alive / 132 gold
- SOCKS5: 283 alive / 155 gold

## Historical pool

- Discovered: 144740
- Ever alive: 25001
- Ever gold: 1053

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
