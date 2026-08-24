# SyndProxy validated proxy pool

## Current pool

- Alive now: 498
- Gold now: 386
- HTTP: 100 alive / 49 gold
- HTTPS: 42 alive / 11 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 187 alive / 166 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33546
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
