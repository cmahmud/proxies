# SyndProxy private pool

## Current pool

- Alive now: 1084
- Gold now: 461
- HTTP: 372 alive / 122 gold
- HTTPS: 255 alive / 72 gold
- SOCKS4: 226 alive / 137 gold
- SOCKS5: 231 alive / 130 gold

## Historical pool

- Discovered: 113568
- Ever alive: 16772
- Ever gold: 623

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
