# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 404
- HTTP: 97 alive / 59 gold
- HTTPS: 52 alive / 16 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36779
- Ever gold: 1279

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
