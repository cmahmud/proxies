# SyndProxy private pool

## Current pool

- Alive now: 900
- Gold now: 427
- HTTP: 269 alive / 98 gold
- HTTPS: 207 alive / 32 gold
- SOCKS4: 183 alive / 138 gold
- SOCKS5: 241 alive / 159 gold

## Historical pool

- Discovered: 161016
- Ever alive: 31077
- Ever gold: 1153

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
