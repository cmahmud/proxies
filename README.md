# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 398
- HTTP: 82 alive / 54 gold
- HTTPS: 45 alive / 16 gold
- SOCKS4: 184 alive / 160 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36672
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
