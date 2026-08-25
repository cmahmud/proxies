# SyndProxy validated proxy pool

## Current pool

- Alive now: 503
- Gold now: 410
- HTTP: 89 alive / 59 gold
- HTTPS: 50 alive / 20 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 192 alive / 169 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36710
- Ever gold: 1277

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
