# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 403
- HTTP: 103 alive / 58 gold
- HTTPS: 51 alive / 18 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 184 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36793
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
