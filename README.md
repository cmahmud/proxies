# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 402
- HTTP: 82 alive / 59 gold
- HTTPS: 64 alive / 12 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36458
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
