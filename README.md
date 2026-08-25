# SyndProxy validated proxy pool

## Current pool

- Alive now: 523
- Gold now: 407
- HTTP: 90 alive / 58 gold
- HTTPS: 62 alive / 18 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 192 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36690
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
