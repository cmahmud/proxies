# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 380
- HTTP: 105 alive / 67 gold
- HTTPS: 64 alive / 17 gold
- SOCKS4: 150 alive / 144 gold
- SOCKS5: 171 alive / 152 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38826
- Ever gold: 1293

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
