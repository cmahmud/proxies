# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 409
- HTTP: 91 alive / 60 gold
- HTTPS: 67 alive / 17 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36349
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
