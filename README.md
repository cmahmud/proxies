# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 401
- HTTP: 97 alive / 60 gold
- HTTPS: 50 alive / 15 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 177 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36779
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
