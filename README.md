# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 391
- HTTP: 93 alive / 54 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36771
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
