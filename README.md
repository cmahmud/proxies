# SyndProxy validated proxy pool

## Current pool

- Alive now: 504
- Gold now: 406
- HTTP: 95 alive / 61 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36733
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
