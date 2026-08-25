# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 403
- HTTP: 111 alive / 60 gold
- HTTPS: 48 alive / 19 gold
- SOCKS4: 176 alive / 160 gold
- SOCKS5: 179 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36798
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
