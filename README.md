# SyndProxy validated proxy pool

## Current pool

- Alive now: 488
- Gold now: 411
- HTTP: 94 alive / 60 gold
- HTTPS: 44 alive / 18 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 183 alive / 173 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36726
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
