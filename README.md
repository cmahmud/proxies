# SyndProxy validated proxy pool

## Current pool

- Alive now: 663
- Gold now: 401
- HTTP: 139 alive / 76 gold
- HTTPS: 180 alive / 27 gold
- SOCKS4: 164 alive / 147 gold
- SOCKS5: 180 alive / 151 gold

## Historical pool

- Discovered: 190445
- Ever alive: 40065
- Ever gold: 1306

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
