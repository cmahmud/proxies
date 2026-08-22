# SyndProxy private pool

## Current pool

- Alive now: 933
- Gold now: 400
- HTTP: 280 alive / 92 gold
- HTTPS: 209 alive / 31 gold
- SOCKS4: 210 alive / 147 gold
- SOCKS5: 234 alive / 130 gold

## Historical pool

- Discovered: 161007
- Ever alive: 31000
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
