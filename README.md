# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 416
- HTTP: 120 alive / 69 gold
- HTTPS: 98 alive / 21 gold
- SOCKS4: 173 alive / 159 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35314
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
