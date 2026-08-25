# SyndProxy validated proxy pool

## Current pool

- Alive now: 484
- Gold now: 401
- HTTP: 75 alive / 52 gold
- HTTPS: 51 alive / 16 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36573
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
