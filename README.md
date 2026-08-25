# SyndProxy validated proxy pool

## Current pool

- Alive now: 463
- Gold now: 400
- HTTP: 75 alive / 55 gold
- HTTPS: 38 alive / 15 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 179 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36607
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
