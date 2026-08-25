# SyndProxy validated proxy pool

## Current pool

- Alive now: 506
- Gold now: 418
- HTTP: 106 alive / 68 gold
- HTTPS: 46 alive / 18 gold
- SOCKS4: 168 alive / 160 gold
- SOCKS5: 186 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36735
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
