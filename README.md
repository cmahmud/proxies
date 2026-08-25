# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 404
- HTTP: 96 alive / 61 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 191 alive / 170 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36437
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
