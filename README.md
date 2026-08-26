# SyndProxy validated proxy pool

## Current pool

- Alive now: 541
- Gold now: 400
- HTTP: 103 alive / 59 gold
- HTTPS: 72 alive / 13 gold
- SOCKS4: 167 alive / 159 gold
- SOCKS5: 199 alive / 169 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38296
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
