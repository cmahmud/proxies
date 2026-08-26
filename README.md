# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 410
- HTTP: 120 alive / 67 gold
- HTTPS: 66 alive / 19 gold
- SOCKS4: 173 alive / 158 gold
- SOCKS5: 195 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38690
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
