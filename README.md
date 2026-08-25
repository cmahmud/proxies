# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 420
- HTTP: 106 alive / 66 gold
- HTTPS: 96 alive / 23 gold
- SOCKS4: 169 alive / 162 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35559
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
