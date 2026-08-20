# SyndProxy private pool

## Current pool

- Alive now: 958
- Gold now: 393
- HTTP: 306 alive / 85 gold
- HTTPS: 207 alive / 24 gold
- SOCKS4: 198 alive / 130 gold
- SOCKS5: 247 alive / 154 gold

## Historical pool

- Discovered: 144740
- Ever alive: 24995
- Ever gold: 1052

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
