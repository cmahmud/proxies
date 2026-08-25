# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 394
- HTTP: 77 alive / 53 gold
- HTTPS: 55 alive / 12 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36539
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
