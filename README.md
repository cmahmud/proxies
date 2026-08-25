# SyndProxy validated proxy pool

## Current pool

- Alive now: 479
- Gold now: 394
- HTTP: 76 alive / 54 gold
- HTTPS: 49 alive / 12 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 181 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36536
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
