# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 411
- HTTP: 93 alive / 61 gold
- HTTPS: 73 alive / 21 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 178 alive / 167 gold

## Historical pool

- Discovered: 184714
- Ever alive: 36907
- Ever gold: 1281

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
