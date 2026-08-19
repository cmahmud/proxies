# SyndProxy private pool

## Current pool

- Alive now: 810
- Gold now: 362
- HTTP: 253 alive / 84 gold
- HTTPS: 160 alive / 16 gold
- SOCKS4: 206 alive / 138 gold
- SOCKS5: 191 alive / 124 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18308
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
