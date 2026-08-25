# SyndProxy validated proxy pool

## Current pool

- Alive now: 519
- Gold now: 410
- HTTP: 92 alive / 61 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 181 alive / 161 gold
- SOCKS5: 192 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36339
- Ever gold: 1272

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
