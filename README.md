# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 398
- HTTP: 100 alive / 60 gold
- HTTPS: 88 alive / 9 gold
- SOCKS4: 176 alive / 161 gold
- SOCKS5: 198 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38224
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
