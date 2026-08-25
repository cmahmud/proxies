# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 412
- HTTP: 88 alive / 60 gold
- HTTPS: 47 alive / 19 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 184 alive / 173 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36729
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
