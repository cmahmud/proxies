# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 399
- HTTP: 94 alive / 57 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36837
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
