# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 425
- HTTP: 110 alive / 75 gold
- HTTPS: 90 alive / 22 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 181 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37867
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
