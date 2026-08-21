# SyndProxy private pool

## Current pool

- Alive now: 846
- Gold now: 372
- HTTP: 258 alive / 92 gold
- HTTPS: 179 alive / 20 gold
- SOCKS4: 201 alive / 148 gold
- SOCKS5: 208 alive / 112 gold

## Historical pool

- Discovered: 154658
- Ever alive: 28937
- Ever gold: 1115

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
