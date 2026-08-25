# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 408
- HTTP: 105 alive / 64 gold
- HTTPS: 97 alive / 20 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 181 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35443
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
