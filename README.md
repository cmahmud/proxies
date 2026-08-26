# SyndProxy validated proxy pool

## Current pool

- Alive now: 546
- Gold now: 429
- HTTP: 102 alive / 77 gold
- HTTPS: 79 alive / 21 gold
- SOCKS4: 188 alive / 164 gold
- SOCKS5: 177 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37899
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
