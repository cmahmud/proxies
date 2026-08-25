# SyndProxy validated proxy pool

## Current pool

- Alive now: 487
- Gold now: 400
- HTTP: 78 alive / 52 gold
- HTTPS: 50 alive / 16 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 182 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36573
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
