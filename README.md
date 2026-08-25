# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 412
- HTTP: 92 alive / 64 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 179 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36892
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
