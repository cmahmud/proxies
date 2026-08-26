# SyndProxy validated proxy pool

## Current pool

- Alive now: 510
- Gold now: 402
- HTTP: 95 alive / 62 gold
- HTTPS: 69 alive / 17 gold
- SOCKS4: 164 alive / 158 gold
- SOCKS5: 182 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38599
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
