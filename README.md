# SyndProxy validated proxy pool

## Current pool

- Alive now: 499
- Gold now: 396
- HTTP: 103 alive / 65 gold
- HTTPS: 48 alive / 16 gold
- SOCKS4: 164 alive / 155 gold
- SOCKS5: 184 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38940
- Ever gold: 1294

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
