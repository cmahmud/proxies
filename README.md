# SyndProxy validated proxy pool

## Current pool

- Alive now: 592
- Gold now: 422
- HTTP: 129 alive / 72 gold
- HTTPS: 91 alive / 24 gold
- SOCKS4: 176 alive / 159 gold
- SOCKS5: 196 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35201
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
