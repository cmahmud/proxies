# SyndProxy validated proxy pool

## Current pool

- Alive now: 512
- Gold now: 393
- HTTP: 95 alive / 65 gold
- HTTPS: 86 alive / 16 gold
- SOCKS4: 169 alive / 157 gold
- SOCKS5: 162 alive / 155 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37462
- Ever gold: 1285

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
