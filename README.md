# SyndProxy validated proxy pool

## Current pool

- Alive now: 528
- Gold now: 409
- HTTP: 89 alive / 61 gold
- HTTPS: 63 alive / 19 gold
- SOCKS4: 180 alive / 160 gold
- SOCKS5: 196 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36692
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
