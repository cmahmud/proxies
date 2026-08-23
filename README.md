# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 341
- HTTP: 97 alive / 30 gold
- HTTPS: 57 alive / 8 gold
- SOCKS4: 187 alive / 149 gold
- SOCKS5: 204 alive / 154 gold

## Historical pool

- Discovered: 172299
- Ever alive: 32956
- Ever gold: 1217

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
