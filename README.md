# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 402
- HTTP: 108 alive / 60 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 175 alive / 160 gold
- SOCKS5: 180 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36798
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
