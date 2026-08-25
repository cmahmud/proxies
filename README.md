# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 412
- HTTP: 93 alive / 61 gold
- HTTPS: 75 alive / 21 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 177 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36908
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
