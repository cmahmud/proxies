# SyndProxy validated proxy pool

## Current pool

- Alive now: 511
- Gold now: 410
- HTTP: 82 alive / 58 gold
- HTTPS: 68 alive / 18 gold
- SOCKS4: 169 alive / 160 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36307
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
