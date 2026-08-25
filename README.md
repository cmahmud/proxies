# SyndProxy validated proxy pool

## Current pool

- Alive now: 565
- Gold now: 426
- HTTP: 104 alive / 64 gold
- HTTPS: 84 alive / 24 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 199 alive / 177 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35950
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
