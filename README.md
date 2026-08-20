# SyndProxy private pool

## Current pool

- Alive now: 800
- Gold now: 350
- HTTP: 207 alive / 75 gold
- HTTPS: 196 alive / 16 gold
- SOCKS4: 201 alive / 132 gold
- SOCKS5: 196 alive / 127 gold

## Historical pool

- Discovered: 149422
- Ever alive: 26546
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
