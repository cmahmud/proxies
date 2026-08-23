# SyndProxy validated proxy pool

## Current pool

- Alive now: 492
- Gold now: 351
- HTTP: 111 alive / 41 gold
- HTTPS: 54 alive / 9 gold
- SOCKS4: 162 alive / 154 gold
- SOCKS5: 165 alive / 147 gold

## Historical pool

- Discovered: 171068
- Ever alive: 32859
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
