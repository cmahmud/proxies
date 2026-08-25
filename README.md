# SyndProxy validated proxy pool

## Current pool

- Alive now: 491
- Gold now: 390
- HTTP: 85 alive / 61 gold
- HTTPS: 75 alive / 17 gold
- SOCKS4: 168 alive / 158 gold
- SOCKS5: 163 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37540
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
