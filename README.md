# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 406
- HTTP: 90 alive / 62 gold
- HTTPS: 86 alive / 16 gold
- SOCKS4: 179 alive / 160 gold
- SOCKS5: 185 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36387
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
