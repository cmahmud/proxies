# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 400
- HTTP: 83 alive / 54 gold
- HTTPS: 54 alive / 17 gold
- SOCKS4: 177 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36654
- Ever gold: 1276

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
