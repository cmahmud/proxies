# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 364
- HTTP: 221 alive / 90 gold
- HTTPS: 143 alive / 24 gold
- SOCKS4: 177 alive / 117 gold
- SOCKS5: 231 alive / 133 gold

## Historical pool

- Discovered: 167408
- Ever alive: 32570
- Ever gold: 1189

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
