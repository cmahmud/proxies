# SyndProxy private pool

## Current pool

- Alive now: 808
- Gold now: 365
- HTTP: 196 alive / 73 gold
- HTTPS: 195 alive / 16 gold
- SOCKS4: 211 alive / 136 gold
- SOCKS5: 206 alive / 140 gold

## Historical pool

- Discovered: 149418
- Ever alive: 26537
- Ever gold: 1082

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
