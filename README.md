# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 400
- HTTP: 92 alive / 55 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 167 alive / 161 gold
- SOCKS5: 181 alive / 166 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36827
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
