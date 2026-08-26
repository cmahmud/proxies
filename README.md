# SyndProxy validated proxy pool

## Current pool

- Alive now: 554
- Gold now: 402
- HTTP: 103 alive / 60 gold
- HTTPS: 86 alive / 15 gold
- SOCKS4: 172 alive / 160 gold
- SOCKS5: 193 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38332
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
