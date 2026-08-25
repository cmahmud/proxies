# SyndProxy validated proxy pool

## Current pool

- Alive now: 500
- Gold now: 402
- HTTP: 88 alive / 57 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 180 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36851
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
