# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 408
- HTTP: 95 alive / 61 gold
- HTTPS: 41 alive / 18 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36741
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
