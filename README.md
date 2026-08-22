# SyndProxy private pool

## Current pool

- Alive now: 920
- Gold now: 384
- HTTP: 298 alive / 88 gold
- HTTPS: 177 alive / 23 gold
- SOCKS4: 191 alive / 115 gold
- SOCKS5: 254 alive / 158 gold

## Historical pool

- Discovered: 166337
- Ever alive: 32397
- Ever gold: 1179

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
