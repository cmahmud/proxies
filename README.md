# SyndProxy validated proxy pool

## Current pool

- Alive now: 522
- Gold now: 410
- HTTP: 85 alive / 61 gold
- HTTPS: 68 alive / 16 gold
- SOCKS4: 179 alive / 161 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36333
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
