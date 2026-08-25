# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 398
- HTTP: 103 alive / 56 gold
- HTTPS: 58 alive / 18 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36824
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
