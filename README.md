# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 400
- HTTP: 78 alive / 56 gold
- HTTPS: 43 alive / 17 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36761
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
