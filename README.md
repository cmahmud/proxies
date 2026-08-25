# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 398
- HTTP: 83 alive / 53 gold
- HTTPS: 52 alive / 17 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36666
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
