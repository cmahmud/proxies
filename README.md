# SyndProxy validated proxy pool

## Current pool

- Alive now: 467
- Gold now: 405
- HTTP: 83 alive / 61 gold
- HTTPS: 39 alive / 17 gold
- SOCKS4: 168 alive / 163 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36751
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
