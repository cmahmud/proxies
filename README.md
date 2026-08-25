# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 398
- HTTP: 80 alive / 60 gold
- HTTPS: 42 alive / 15 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36757
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
