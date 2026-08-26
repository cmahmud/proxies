# SyndProxy validated proxy pool

## Current pool

- Alive now: 539
- Gold now: 404
- HTTP: 109 alive / 65 gold
- HTTPS: 73 alive / 18 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 185 alive / 163 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38741
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
