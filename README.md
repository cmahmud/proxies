# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 410
- HTTP: 101 alive / 67 gold
- HTTPS: 87 alive / 19 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35428
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
