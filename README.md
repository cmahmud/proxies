# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 407
- HTTP: 102 alive / 60 gold
- HTTPS: 48 alive / 18 gold
- SOCKS4: 177 alive / 159 gold
- SOCKS5: 189 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36703
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
