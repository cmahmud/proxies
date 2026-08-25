# SyndProxy validated proxy pool

## Current pool

- Alive now: 502
- Gold now: 412
- HTTP: 82 alive / 65 gold
- HTTPS: 61 alive / 17 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 184 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36382
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
