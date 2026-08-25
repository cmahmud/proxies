# SyndProxy validated proxy pool

## Current pool

- Alive now: 553
- Gold now: 404
- HTTP: 113 alive / 61 gold
- HTTPS: 83 alive / 19 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35450
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
