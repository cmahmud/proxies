# SyndProxy validated proxy pool

## Current pool

- Alive now: 526
- Gold now: 406
- HTTP: 114 alive / 59 gold
- HTTPS: 60 alive / 20 gold
- SOCKS4: 174 alive / 161 gold
- SOCKS5: 178 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36814
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
