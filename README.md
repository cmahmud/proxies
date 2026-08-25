# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 401
- HTTP: 85 alive / 56 gold
- HTTPS: 56 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 179 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36594
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
