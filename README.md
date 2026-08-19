# SyndProxy private pool

## Current pool

- Alive now: 901
- Gold now: 399
- HTTP: 268 alive / 92 gold
- HTTPS: 195 alive / 15 gold
- SOCKS4: 237 alive / 156 gold
- SOCKS5: 201 alive / 136 gold

## Historical pool

- Discovered: 119831
- Ever alive: 18263
- Ever gold: 718

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
