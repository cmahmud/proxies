# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 404
- HTTP: 99 alive / 64 gold
- HTTPS: 67 alive / 18 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 195 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38696
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
