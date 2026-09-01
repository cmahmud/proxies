# SyndProxy validated proxy pool

## Current pool

- Alive now: 645
- Gold now: 461
- HTTP: 139 alive / 90 gold
- HTTPS: 121 alive / 32 gold
- SOCKS4: 183 alive / 163 gold
- SOCKS5: 202 alive / 176 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46299
- Ever gold: 1443

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
