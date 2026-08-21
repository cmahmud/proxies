# SyndProxy private pool

## Current pool

- Alive now: 1011
- Gold now: 365
- HTTP: 349 alive / 84 gold
- HTTPS: 223 alive / 19 gold
- SOCKS4: 221 alive / 119 gold
- SOCKS5: 218 alive / 143 gold

## Historical pool

- Discovered: 158214
- Ever alive: 29806
- Ever gold: 1137

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
