# SyndProxy validated proxy pool

## Current pool

- Alive now: 520
- Gold now: 403
- HTTP: 92 alive / 61 gold
- HTTPS: 67 alive / 16 gold
- SOCKS4: 167 alive / 160 gold
- SOCKS5: 194 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38458
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
