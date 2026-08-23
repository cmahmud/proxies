# SyndProxy validated proxy pool

## Current pool

- Alive now: 396
- Gold now: 222
- HTTP: 147 alive / 60 gold
- HTTPS: 52 alive / 12 gold
- SOCKS4: 76 alive / 68 gold
- SOCKS5: 121 alive / 82 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32687
- Ever gold: 1206

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
