# SyndProxy private pool

## Current pool

- Alive now: 839
- Gold now: 404
- HTTP: 226 alive / 76 gold
- HTTPS: 191 alive / 19 gold
- SOCKS4: 209 alive / 156 gold
- SOCKS5: 213 alive / 153 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26805
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
