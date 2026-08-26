# SyndProxy validated proxy pool

## Current pool

- Alive now: 517
- Gold now: 404
- HTTP: 109 alive / 64 gold
- HTTPS: 57 alive / 18 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 183 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38954
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
