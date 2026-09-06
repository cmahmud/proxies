# SyndProxy validated proxy pool

## Current pool

- Alive now: 451
- Gold now: 371
- HTTP: 78 alive / 49 gold
- HTTPS: 28 alive / 12 gold
- SOCKS4: 166 alive / 156 gold
- SOCKS5: 179 alive / 154 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48307
- Ever gold: 1527

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
