# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 411
- HTTP: 88 alive / 62 gold
- HTTPS: 60 alive / 16 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 192 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36330
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
