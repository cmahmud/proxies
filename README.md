# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 398
- HTTP: 82 alive / 58 gold
- HTTPS: 51 alive / 14 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36471
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
