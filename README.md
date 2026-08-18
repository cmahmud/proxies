# SyndProxy private pool

## Current pool

- Alive now: 836
- Gold now: 256
- HTTP: 252 alive / 27 gold
- HTTPS: 150 alive / 3 gold
- SOCKS4: 211 alive / 117 gold
- SOCKS5: 223 alive / 109 gold

## Historical pool

- Discovered: 99142
- Ever alive: 12059
- Ever gold: 390

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
