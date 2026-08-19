# SyndProxy private pool

## Current pool

- Alive now: 1157
- Gold now: 545
- HTTP: 440 alive / 157 gold
- HTTPS: 292 alive / 106 gold
- SOCKS4: 217 alive / 133 gold
- SOCKS5: 208 alive / 149 gold

## Historical pool

- Discovered: 127353
- Ever alive: 19836
- Ever gold: 803

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
