# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 414
- HTTP: 94 alive / 63 gold
- HTTPS: 42 alive / 19 gold
- SOCKS4: 170 alive / 162 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36743
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
