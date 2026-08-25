# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 403
- HTTP: 108 alive / 58 gold
- HTTPS: 51 alive / 19 gold
- SOCKS4: 173 alive / 161 gold
- SOCKS5: 180 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36814
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
