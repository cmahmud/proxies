# SyndProxy private pool

## Current pool

- Alive now: 819
- Gold now: 363
- HTTP: 255 alive / 85 gold
- HTTPS: 158 alive / 16 gold
- SOCKS4: 210 alive / 138 gold
- SOCKS5: 196 alive / 124 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18315
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
