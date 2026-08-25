# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 404
- HTTP: 106 alive / 59 gold
- HTTPS: 52 alive / 18 gold
- SOCKS4: 174 alive / 160 gold
- SOCKS5: 183 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36795
- Ever gold: 1280

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
