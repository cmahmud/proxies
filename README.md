# SyndProxy private pool

## Current pool

- Alive now: 1126
- Gold now: 390
- HTTP: 375 alive / 86 gold
- HTTPS: 284 alive / 14 gold
- SOCKS4: 216 alive / 127 gold
- SOCKS5: 251 alive / 163 gold

## Historical pool

- Discovered: 131855
- Ever alive: 21288
- Ever gold: 880

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
