# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 400
- HTTP: 85 alive / 53 gold
- HTTPS: 46 alive / 16 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36599
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
