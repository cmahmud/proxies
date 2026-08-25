# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 400
- HTTP: 91 alive / 63 gold
- HTTPS: 43 alive / 15 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 179 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36757
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
