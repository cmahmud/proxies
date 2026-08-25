# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 404
- HTTP: 92 alive / 59 gold
- HTTPS: 57 alive / 17 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 185 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36868
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
