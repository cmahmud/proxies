# SyndProxy validated proxy pool

## Current pool

- Alive now: 531
- Gold now: 400
- HTTP: 103 alive / 58 gold
- HTTPS: 67 alive / 15 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 190 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39059
- Ever gold: 1296

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
