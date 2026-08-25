# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 400
- HTTP: 94 alive / 56 gold
- HTTPS: 62 alive / 16 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36850
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
