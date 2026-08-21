# SyndProxy private pool

## Current pool

- Alive now: 821
- Gold now: 397
- HTTP: 230 alive / 77 gold
- HTTPS: 148 alive / 16 gold
- SOCKS4: 199 alive / 146 gold
- SOCKS5: 244 alive / 158 gold

## Historical pool

- Discovered: 155790
- Ever alive: 29323
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
