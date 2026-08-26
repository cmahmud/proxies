# SyndProxy validated proxy pool

## Current pool

- Alive now: 579
- Gold now: 404
- HTTP: 106 alive / 60 gold
- HTTPS: 104 alive / 12 gold
- SOCKS4: 176 alive / 162 gold
- SOCKS5: 193 alive / 170 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38142
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
