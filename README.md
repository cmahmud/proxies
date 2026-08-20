# SyndProxy private pool

## Current pool

- Alive now: 732
- Gold now: 375
- HTTP: 166 alive / 72 gold
- HTTPS: 135 alive / 18 gold
- SOCKS4: 232 alive / 149 gold
- SOCKS5: 199 alive / 136 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26256
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
