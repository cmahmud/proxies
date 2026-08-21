# SyndProxy private pool

## Current pool

- Alive now: 988
- Gold now: 429
- HTTP: 315 alive / 109 gold
- HTTPS: 193 alive / 30 gold
- SOCKS4: 231 alive / 148 gold
- SOCKS5: 249 alive / 142 gold

## Historical pool

- Discovered: 160278
- Ever alive: 30762
- Ever gold: 1147

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
