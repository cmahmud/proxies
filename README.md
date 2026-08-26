# SyndProxy validated proxy pool

## Current pool

- Alive now: 548
- Gold now: 410
- HTTP: 100 alive / 66 gold
- HTTPS: 85 alive / 15 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 187 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38096
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
