# SyndProxy private pool

## Current pool

- Alive now: 1214
- Gold now: 530
- HTTP: 453 alive / 154 gold
- HTTPS: 331 alive / 106 gold
- SOCKS4: 232 alive / 143 gold
- SOCKS5: 198 alive / 127 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19945
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
