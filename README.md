# SyndProxy validated proxy pool

## Current pool

- Alive now: 478
- Gold now: 397
- HTTP: 87 alive / 53 gold
- HTTPS: 40 alive / 18 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 179 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36762
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
