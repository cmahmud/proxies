# SyndProxy private pool

## Current pool

- Alive now: 970
- Gold now: 389
- HTTP: 331 alive / 84 gold
- HTTPS: 186 alive / 27 gold
- SOCKS4: 212 alive / 145 gold
- SOCKS5: 241 alive / 133 gold

## Historical pool

- Discovered: 167116
- Ever alive: 32527
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
