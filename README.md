# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 390
- HTTP: 345 alive / 86 gold
- HTTPS: 257 alive / 19 gold
- SOCKS4: 229 alive / 147 gold
- SOCKS5: 253 alive / 138 gold

## Historical pool

- Discovered: 158238
- Ever alive: 30002
- Ever gold: 1139

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
