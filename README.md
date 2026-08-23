# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 349
- HTTP: 96 alive / 38 gold
- HTTPS: 46 alive / 10 gold
- SOCKS4: 161 alive / 153 gold
- SOCKS5: 166 alive / 148 gold

## Historical pool

- Discovered: 171068
- Ever alive: 32858
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
