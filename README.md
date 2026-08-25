# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 417
- HTTP: 90 alive / 63 gold
- HTTPS: 73 alive / 20 gold
- SOCKS4: 171 alive / 162 gold
- SOCKS5: 190 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 36250
- Ever gold: 1270

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
