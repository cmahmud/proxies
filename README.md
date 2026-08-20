# SyndProxy private pool

## Current pool

- Alive now: 911
- Gold now: 350
- HTTP: 261 alive / 75 gold
- HTTPS: 255 alive / 16 gold
- SOCKS4: 201 alive / 132 gold
- SOCKS5: 194 alive / 127 gold

## Historical pool

- Discovered: 149491
- Ever alive: 26563
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
