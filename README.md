# SyndProxy validated proxy pool

## Current pool

- Alive now: 550
- Gold now: 424
- HTTP: 106 alive / 74 gold
- HTTPS: 87 alive / 21 gold
- SOCKS4: 182 alive / 164 gold
- SOCKS5: 175 alive / 165 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37853
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
