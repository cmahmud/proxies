# SyndProxy validated proxy pool

## Current pool

- Alive now: 465
- Gold now: 388
- HTTP: 81 alive / 53 gold
- HTTPS: 39 alive / 13 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 176 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36763
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
