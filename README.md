# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 408
- HTTP: 94 alive / 62 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36366
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
