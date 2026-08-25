# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 399
- HTTP: 81 alive / 59 gold
- HTTPS: 45 alive / 14 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36468
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
