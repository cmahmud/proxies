# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 396
- HTTP: 93 alive / 53 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36829
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
