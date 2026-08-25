# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 398
- HTTP: 95 alive / 55 gold
- HTTPS: 57 alive / 16 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36848
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
