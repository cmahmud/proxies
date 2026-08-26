# SyndProxy validated proxy pool

## Current pool

- Alive now: 529
- Gold now: 406
- HTTP: 95 alive / 64 gold
- HTTPS: 73 alive / 17 gold
- SOCKS4: 173 alive / 160 gold
- SOCKS5: 188 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38485
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
