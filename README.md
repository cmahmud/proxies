# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 411
- HTTP: 79 alive / 58 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 169 alive / 161 gold
- SOCKS5: 192 alive / 174 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36305
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
