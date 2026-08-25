# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 399
- HTTP: 83 alive / 58 gold
- HTTPS: 56 alive / 15 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 182 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36476
- Ever gold: 1274

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
