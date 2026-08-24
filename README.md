# SyndProxy validated proxy pool

## Current pool

- Alive now: 493
- Gold now: 386
- HTTP: 96 alive / 48 gold
- HTTPS: 40 alive / 12 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 180270
- Ever alive: 33545
- Ever gold: 1241

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
