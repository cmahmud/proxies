# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 395
- HTTP: 103 alive / 55 gold
- HTTPS: 60 alive / 17 gold
- SOCKS4: 171 alive / 160 gold
- SOCKS5: 180 alive / 163 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36824
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
