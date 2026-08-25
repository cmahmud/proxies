# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 391
- HTTP: 90 alive / 54 gold
- HTTPS: 45 alive / 15 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 177 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36772
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
