# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 411
- HTTP: 96 alive / 60 gold
- HTTPS: 86 alive / 21 gold
- SOCKS4: 173 alive / 162 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36920
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
