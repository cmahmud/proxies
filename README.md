# SyndProxy validated proxy pool

## Current pool

- Alive now: 518
- Gold now: 412
- HTTP: 99 alive / 65 gold
- HTTPS: 70 alive / 20 gold
- SOCKS4: 166 alive / 159 gold
- SOCKS5: 183 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38633
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
