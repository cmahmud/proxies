# SyndProxy private pool

## Current pool

- Alive now: 972
- Gold now: 385
- HTTP: 338 alive / 88 gold
- HTTPS: 168 alive / 22 gold
- SOCKS4: 194 alive / 115 gold
- SOCKS5: 272 alive / 160 gold

## Historical pool

- Discovered: 166337
- Ever alive: 32397
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
