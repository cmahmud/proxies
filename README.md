# SyndProxy private pool

## Current pool

- Alive now: 835
- Gold now: 391
- HTTP: 226 alive / 78 gold
- HTTPS: 141 alive / 21 gold
- SOCKS4: 245 alive / 157 gold
- SOCKS5: 223 alive / 135 gold

## Historical pool

- Discovered: 156830
- Ever alive: 29625
- Ever gold: 1133

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
