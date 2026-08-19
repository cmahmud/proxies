# SyndProxy private pool

## Current pool

- Alive now: 1216
- Gold now: 535
- HTTP: 438 alive / 156 gold
- HTTPS: 339 alive / 109 gold
- SOCKS4: 247 alive / 143 gold
- SOCKS5: 192 alive / 127 gold

## Historical pool

- Discovered: 127372
- Ever alive: 19945
- Ever gold: 804

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
