# SyndProxy validated proxy pool

## Current pool

- Alive now: 585
- Gold now: 418
- HTTP: 107 alive / 60 gold
- HTTPS: 104 alive / 25 gold
- SOCKS4: 178 alive / 161 gold
- SOCKS5: 196 alive / 172 gold

## Historical pool

- Discovered: 183892
- Ever alive: 35809
- Ever gold: 1261

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
