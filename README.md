# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 408
- HTTP: 93 alive / 58 gold
- HTTPS: 52 alive / 19 gold
- SOCKS4: 174 alive / 163 gold
- SOCKS5: 188 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36717
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
