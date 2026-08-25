# SyndProxy validated proxy pool

## Current pool

- Alive now: 581
- Gold now: 422
- HTTP: 126 alive / 73 gold
- HTTPS: 84 alive / 23 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 197 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35206
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
