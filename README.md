# SyndProxy private pool

## Current pool

- Alive now: 1003
- Gold now: 394
- HTTP: 361 alive / 73 gold
- HTTPS: 204 alive / 18 gold
- SOCKS4: 209 alive / 154 gold
- SOCKS5: 229 alive / 149 gold

## Historical pool

- Discovered: 149509
- Ever alive: 26791
- Ever gold: 1087

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
