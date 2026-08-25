# SyndProxy validated proxy pool

## Current pool

- Alive now: 509
- Gold now: 400
- HTTP: 102 alive / 57 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 178 alive / 164 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36818
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
