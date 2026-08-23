# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 393
- HTTP: 102 alive / 62 gold
- HTTPS: 46 alive / 15 gold
- SOCKS4: 167 alive / 154 gold
- SOCKS5: 188 alive / 162 gold

## Historical pool

- Discovered: 175438
- Ever alive: 33155
- Ever gold: 1228

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
