# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 414
- HTTP: 92 alive / 63 gold
- HTTPS: 63 alive / 22 gold
- SOCKS4: 177 alive / 160 gold
- SOCKS5: 183 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36941
- Ever gold: 1282

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
