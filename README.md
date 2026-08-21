# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 400
- HTTP: 287 alive / 86 gold
- HTTPS: 165 alive / 26 gold
- SOCKS4: 227 alive / 141 gold
- SOCKS5: 232 alive / 147 gold

## Historical pool

- Discovered: 157420
- Ever alive: 29724
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
