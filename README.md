# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 404
- HTTP: 109 alive / 59 gold
- HTTPS: 53 alive / 18 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36806
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
