# SyndProxy private pool

## Current pool

- Alive now: 1010
- Gold now: 356
- HTTP: 332 alive / 73 gold
- HTTPS: 221 alive / 18 gold
- SOCKS4: 209 alive / 122 gold
- SOCKS5: 248 alive / 143 gold

## Historical pool

- Discovered: 110856
- Ever alive: 15788
- Ever gold: 504

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
