# SyndProxy validated proxy pool

## Current pool

- Alive now: 516
- Gold now: 402
- HTTP: 103 alive / 69 gold
- HTTPS: 68 alive / 15 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 173 alive / 160 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37320
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
