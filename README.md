# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 401
- HTTP: 98 alive / 59 gold
- HTTPS: 52 alive / 15 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 177 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36779
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
