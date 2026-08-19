# SyndProxy private pool

## Current pool

- Alive now: 1040
- Gold now: 555
- HTTP: 364 alive / 165 gold
- HTTPS: 223 alive / 92 gold
- SOCKS4: 241 alive / 151 gold
- SOCKS5: 212 alive / 147 gold

## Historical pool

- Discovered: 124833
- Ever alive: 19173
- Ever gold: 731

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
