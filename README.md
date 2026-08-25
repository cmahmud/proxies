# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 405
- HTTP: 95 alive / 61 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36438
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
