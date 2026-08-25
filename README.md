# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 399
- HTTP: 84 alive / 54 gold
- HTTPS: 49 alive / 16 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 185 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36585
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
