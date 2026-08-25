# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 416
- HTTP: 96 alive / 66 gold
- HTTPS: 67 alive / 23 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36941
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
