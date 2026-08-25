# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 412
- HTTP: 97 alive / 60 gold
- HTTPS: 86 alive / 22 gold
- SOCKS4: 168 alive / 162 gold
- SOCKS5: 178 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36920
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
