# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 346
- HTTP: 126 alive / 38 gold
- HTTPS: 82 alive / 5 gold
- SOCKS4: 165 alive / 152 gold
- SOCKS5: 193 alive / 151 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32911
- Ever gold: 1214

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
