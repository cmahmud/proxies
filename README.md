# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 392
- HTTP: 75 alive / 51 gold
- HTTPS: 35 alive / 14 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36581
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
