# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 406
- HTTP: 92 alive / 62 gold
- HTTPS: 52 alive / 15 gold
- SOCKS4: 175 alive / 159 gold
- SOCKS5: 190 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36436
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
