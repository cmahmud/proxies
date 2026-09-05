# SyndProxy validated proxy pool

## Current pool

- Alive now: 429
- Gold now: 313
- HTTP: 126 alive / 76 gold
- HTTPS: 33 alive / 19 gold
- SOCKS4: 90 alive / 71 gold
- SOCKS5: 180 alive / 147 gold

## Historical pool

- Discovered: 218933
- Ever alive: 47819
- Ever gold: 1487

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
