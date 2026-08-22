# SyndProxy private pool

## Current pool

- Alive now: 937
- Gold now: 397
- HTTP: 293 alive / 83 gold
- HTTPS: 190 alive / 25 gold
- SOCKS4: 199 alive / 134 gold
- SOCKS5: 255 alive / 155 gold

## Historical pool

- Discovered: 163866
- Ever alive: 31988
- Ever gold: 1170

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
