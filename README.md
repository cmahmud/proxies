# SyndProxy private pool

## Current pool

- Alive now: 720
- Gold now: 371
- HTTP: 160 alive / 72 gold
- HTTPS: 144 alive / 16 gold
- SOCKS4: 223 alive / 146 gold
- SOCKS5: 193 alive / 137 gold

## Historical pool

- Discovered: 148336
- Ever alive: 26264
- Ever gold: 1080

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
