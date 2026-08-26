# SyndProxy validated proxy pool

## Current pool

- Alive now: 540
- Gold now: 402
- HTTP: 93 alive / 61 gold
- HTTPS: 85 alive / 14 gold
- SOCKS4: 175 alive / 162 gold
- SOCKS5: 187 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39161
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
