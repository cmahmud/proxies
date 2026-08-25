# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 419
- HTTP: 100 alive / 70 gold
- HTTPS: 90 alive / 21 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35425
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
