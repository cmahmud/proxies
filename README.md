# SyndProxy private pool

## Current pool

- Alive now: 1015
- Gold now: 401
- HTTP: 353 alive / 75 gold
- HTTPS: 223 alive / 20 gold
- SOCKS4: 214 alive / 155 gold
- SOCKS5: 225 alive / 151 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26799
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
