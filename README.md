# SyndProxy private pool

## Current pool

- Alive now: 967
- Gold now: 390
- HTTP: 336 alive / 86 gold
- HTTPS: 172 alive / 26 gold
- SOCKS4: 222 alive / 145 gold
- SOCKS5: 237 alive / 133 gold

## Historical pool

- Discovered: 167116
- Ever alive: 32527
- Ever gold: 1185

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
