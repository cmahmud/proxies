# SyndProxy validated proxy pool

## Current pool

- Alive now: 521
- Gold now: 402
- HTTP: 99 alive / 62 gold
- HTTPS: 67 alive / 20 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 184 alive / 162 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38714
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
