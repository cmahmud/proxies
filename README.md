# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 413
- HTTP: 96 alive / 60 gold
- HTTPS: 68 alive / 20 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 194 alive / 171 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36240
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
