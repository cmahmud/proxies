# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 409
- HTTP: 99 alive / 60 gold
- HTTPS: 49 alive / 18 gold
- SOCKS4: 178 alive / 160 gold
- SOCKS5: 190 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36705
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
