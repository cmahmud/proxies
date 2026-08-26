# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 399
- HTTP: 99 alive / 60 gold
- HTTPS: 79 alive / 10 gold
- SOCKS4: 171 alive / 161 gold
- SOCKS5: 198 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38222
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
