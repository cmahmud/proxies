# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 404
- HTTP: 91 alive / 65 gold
- HTTPS: 87 alive / 18 gold
- SOCKS4: 164 alive / 157 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34971
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
