# SyndProxy private pool

## Current pool

- Alive now: 999
- Gold now: 400
- HTTP: 351 alive / 75 gold
- HTTPS: 211 alive / 20 gold
- SOCKS4: 212 alive / 155 gold
- SOCKS5: 225 alive / 150 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26799
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
