# SyndProxy validated proxy pool

## Current pool

- Alive now: 547
- Gold now: 407
- HTTP: 110 alive / 65 gold
- HTTPS: 74 alive / 19 gold
- SOCKS4: 172 alive / 158 gold
- SOCKS5: 191 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38671
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
