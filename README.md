# SyndProxy validated proxy pool

## Current pool

- Alive now: 544
- Gold now: 418
- HTTP: 97 alive / 63 gold
- HTTPS: 89 alive / 23 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35588
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
