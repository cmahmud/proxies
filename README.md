# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 407
- HTTP: 93 alive / 59 gold
- HTTPS: 56 alive / 19 gold
- SOCKS4: 169 alive / 159 gold
- SOCKS5: 186 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36733
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
