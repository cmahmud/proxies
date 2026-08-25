# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 417
- HTTP: 105 alive / 67 gold
- HTTPS: 45 alive / 18 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 185 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36734
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
