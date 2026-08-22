# SyndProxy private pool

## Current pool

- Alive now: 886
- Gold now: 377
- HTTP: 282 alive / 70 gold
- HTTPS: 175 alive / 25 gold
- SOCKS4: 202 alive / 125 gold
- SOCKS5: 227 alive / 157 gold

## Historical pool

- Discovered: 164971
- Ever alive: 32252
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
