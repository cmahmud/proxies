# SyndProxy validated proxy pool

## Current pool

- Alive now: 489
- Gold now: 401
- HTTP: 98 alive / 59 gold
- HTTPS: 44 alive / 16 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 176 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36779
- Ever gold: 1278

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
