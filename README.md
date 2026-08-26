# SyndProxy validated proxy pool

## Current pool

- Alive now: 482
- Gold now: 372
- HTTP: 93 alive / 58 gold
- HTTPS: 56 alive / 17 gold
- SOCKS4: 160 alive / 143 gold
- SOCKS5: 173 alive / 154 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38887
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
