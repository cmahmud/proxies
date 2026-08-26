# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 402
- HTTP: 90 alive / 60 gold
- HTTPS: 64 alive / 16 gold
- SOCKS4: 166 alive / 160 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38457
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
