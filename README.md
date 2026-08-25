# SyndProxy validated proxy pool

## Current pool

- Alive now: 462
- Gold now: 394
- HTTP: 73 alive / 51 gold
- HTTPS: 37 alive / 15 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 184 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36579
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
