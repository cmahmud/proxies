# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 365
- HTTP: 251 alive / 87 gold
- HTTPS: 159 alive / 16 gold
- SOCKS4: 202 alive / 138 gold
- SOCKS5: 188 alive / 124 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18307
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
