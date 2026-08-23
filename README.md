# SyndProxy validated proxy pool

## Current pool

- Alive now: 524
- Gold now: 362
- HTTP: 111 alive / 38 gold
- HTTPS: 58 alive / 10 gold
- SOCKS4: 168 alive / 159 gold
- SOCKS5: 187 alive / 155 gold

## Historical pool

- Discovered: 171582
- Ever alive: 32925
- Ever gold: 1216

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
