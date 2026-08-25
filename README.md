# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 404
- HTTP: 92 alive / 59 gold
- HTTPS: 64 alive / 18 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 181 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36853
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
