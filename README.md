# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 414
- HTTP: 101 alive / 68 gold
- HTTPS: 46 alive / 17 gold
- SOCKS4: 169 alive / 158 gold
- SOCKS5: 183 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36737
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
