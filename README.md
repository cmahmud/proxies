# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 398
- HTTP: 103 alive / 67 gold
- HTTPS: 80 alive / 18 gold
- SOCKS4: 166 alive / 157 gold
- SOCKS5: 171 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37428
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
