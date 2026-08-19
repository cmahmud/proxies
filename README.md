# SyndProxy private pool

## Current pool

- Alive now: 1230
- Gold now: 542
- HTTP: 443 alive / 183 gold
- HTTPS: 333 alive / 68 gold
- SOCKS4: 207 alive / 124 gold
- SOCKS5: 247 alive / 167 gold

## Historical pool

- Discovered: 125671
- Ever alive: 19662
- Ever gold: 774

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
