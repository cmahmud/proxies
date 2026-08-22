# SyndProxy private pool

## Current pool

- Alive now: 892
- Gold now: 377
- HTTP: 280 alive / 73 gold
- HTTPS: 190 alive / 23 gold
- SOCKS4: 193 alive / 124 gold
- SOCKS5: 229 alive / 157 gold

## Historical pool

- Discovered: 164972
- Ever alive: 32256
- Ever gold: 1177

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
