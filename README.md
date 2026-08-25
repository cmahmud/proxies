# SyndProxy validated proxy pool

## Current pool

- Alive now: 469
- Gold now: 395
- HTTP: 77 alive / 55 gold
- HTTPS: 41 alive / 19 gold
- SOCKS4: 171 alive / 157 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36761
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
