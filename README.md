# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 399
- HTTP: 81 alive / 54 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36617
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
