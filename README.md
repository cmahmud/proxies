# SyndProxy validated proxy pool

## Current pool

- Alive now: 496
- Gold now: 384
- HTTP: 110 alive / 67 gold
- HTTPS: 51 alive / 17 gold
- SOCKS4: 159 alive / 144 gold
- SOCKS5: 176 alive / 156 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38919
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
