# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 417
- HTTP: 98 alive / 62 gold
- HTTPS: 82 alive / 20 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 188 alive / 173 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35600
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
