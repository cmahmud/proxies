# SyndProxy validated proxy pool

## Current pool

- Alive now: 486
- Gold now: 396
- HTTP: 90 alive / 56 gold
- HTTPS: 46 alive / 16 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36775
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
