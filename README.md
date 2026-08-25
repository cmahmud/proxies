# SyndProxy validated proxy pool

## Current pool

- Alive now: 497
- Gold now: 416
- HTTP: 93 alive / 63 gold
- HTTPS: 50 alive / 20 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36745
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
