# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 404
- HTTP: 89 alive / 59 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 170 alive / 160 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 190445
- Ever alive: 42752
- Ever gold: 1361

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
