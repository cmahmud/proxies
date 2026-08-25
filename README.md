# SyndProxy validated proxy pool

## Current pool

- Alive now: 466
- Gold now: 400
- HTTP: 73 alive / 58 gold
- HTTPS: 41 alive / 12 gold
- SOCKS4: 170 alive / 159 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36522
- Ever gold: 1275

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
