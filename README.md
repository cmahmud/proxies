# SyndProxy validated proxy pool

## Current pool

- Alive now: 513
- Gold now: 414
- HTTP: 85 alive / 57 gold
- HTTPS: 60 alive / 19 gold
- SOCKS4: 177 alive / 163 gold
- SOCKS5: 191 alive / 175 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36291
- Ever gold: 1271

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
