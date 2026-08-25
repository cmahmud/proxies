# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 400
- HTTP: 91 alive / 55 gold
- HTTPS: 43 alive / 16 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 189 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36680
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
