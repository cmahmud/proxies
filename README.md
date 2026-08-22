# SyndProxy private pool

## Current pool

- Alive now: 834
- Gold now: 353
- HTTP: 252 alive / 79 gold
- HTTPS: 161 alive / 23 gold
- SOCKS4: 188 alive / 118 gold
- SOCKS5: 233 alive / 133 gold

## Historical pool

- Discovered: 167924
- Ever alive: 32595
- Ever gold: 1190

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
