# SyndProxy validated proxy pool

## Current pool

- Alive now: 533
- Gold now: 399
- HTTP: 97 alive / 58 gold
- HTTPS: 76 alive / 17 gold
- SOCKS4: 171 alive / 158 gold
- SOCKS5: 189 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38566
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
