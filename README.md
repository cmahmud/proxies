# SyndProxy private pool

## Current pool

- Alive now: 736
- Gold now: 379
- HTTP: 173 alive / 74 gold
- HTTPS: 136 alive / 19 gold
- SOCKS4: 230 alive / 149 gold
- SOCKS5: 197 alive / 137 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26247
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
