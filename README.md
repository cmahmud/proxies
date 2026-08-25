# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 404
- HTTP: 103 alive / 59 gold
- HTTPS: 53 alive / 16 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36783
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
