# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 403
- HTTP: 110 alive / 59 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 178 alive / 165 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36803
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
