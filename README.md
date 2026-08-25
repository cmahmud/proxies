# SyndProxy validated proxy pool

## Current pool

- Alive now: 589
- Gold now: 420
- HTTP: 115 alive / 71 gold
- HTTPS: 111 alive / 22 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 186 alive / 168 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35072
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
