# SyndProxy validated proxy pool

## Current pool

- Alive now: 549
- Gold now: 404
- HTTP: 93 alive / 61 gold
- HTTPS: 93 alive / 15 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 188 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39164
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
