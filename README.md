# SyndProxy private pool

## Current pool

- Alive now: 1031
- Gold now: 552
- HTTP: 366 alive / 167 gold
- HTTPS: 226 alive / 92 gold
- SOCKS4: 229 alive / 147 gold
- SOCKS5: 210 alive / 146 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19171
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
