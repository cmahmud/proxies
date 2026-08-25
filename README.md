# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 407
- HTTP: 84 alive / 60 gold
- HTTPS: 60 alive / 18 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36364
- Ever gold: 1273

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
