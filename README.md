# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 400
- HTTP: 101 alive / 56 gold
- HTTPS: 50 alive / 19 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 184 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36833
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
