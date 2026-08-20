# SyndProxy private pool

## Current pool

- Alive now: 694
- Gold now: 353
- HTTP: 171 alive / 72 gold
- HTTPS: 127 alive / 19 gold
- SOCKS4: 220 alive / 145 gold
- SOCKS5: 176 alive / 117 gold

## Historical pool

- Discovered: 145543
- Ever alive: 25350
- Ever gold: 1058

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
