# SyndProxy private pool

## Current pool

- Alive now: 987
- Gold now: 397
- HTTP: 318 alive / 90 gold
- HTTPS: 209 alive / 25 gold
- SOCKS4: 203 alive / 112 gold
- SOCKS5: 257 alive / 170 gold

## Historical pool

- Discovered: 166616
- Ever alive: 32440
- Ever gold: 1182

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
