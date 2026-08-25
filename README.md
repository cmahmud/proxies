# SyndProxy validated proxy pool

## Current pool

- Alive now: 495
- Gold now: 410
- HTTP: 98 alive / 60 gold
- HTTPS: 46 alive / 18 gold
- SOCKS4: 166 alive / 161 gold
- SOCKS5: 185 alive / 171 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36725
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
