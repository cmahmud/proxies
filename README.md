# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 384
- HTTP: 88 alive / 57 gold
- HTTPS: 72 alive / 13 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 174 alive / 157 gold

## Historical pool

- Discovered: 190445
- Ever alive: 43428
- Ever gold: 1371

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
