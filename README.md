# SyndProxy validated proxy pool

## Current pool

- Alive now: 525
- Gold now: 400
- HTTP: 96 alive / 59 gold
- HTTPS: 72 alive / 16 gold
- SOCKS4: 174 alive / 159 gold
- SOCKS5: 183 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38561
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
