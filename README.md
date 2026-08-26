# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 409
- HTTP: 106 alive / 65 gold
- HTTPS: 73 alive / 21 gold
- SOCKS4: 176 alive / 158 gold
- SOCKS5: 195 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38750
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
