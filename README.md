# SyndProxy validated proxy pool

## Current pool

- Alive now: 508
- Gold now: 407
- HTTP: 80 alive / 59 gold
- HTTPS: 65 alive / 18 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 190 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36358
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
