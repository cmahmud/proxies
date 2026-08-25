# SyndProxy validated proxy pool

## Current pool

- Alive now: 494
- Gold now: 398
- HTTP: 85 alive / 53 gold
- HTTPS: 44 alive / 17 gold
- SOCKS4: 181 alive / 160 gold
- SOCKS5: 184 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36677
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
