# SyndProxy validated proxy pool

## Current pool

- Alive now: 556
- Gold now: 419
- HTTP: 117 alive / 69 gold
- HTTPS: 78 alive / 21 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35329
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
