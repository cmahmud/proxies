# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 422
- HTTP: 109 alive / 73 gold
- HTTPS: 93 alive / 21 gold
- SOCKS4: 185 alive / 164 gold
- SOCKS5: 182 alive / 164 gold

## Historical pool

- Discovered: 185576
- Ever alive: 37868
- Ever gold: 1288

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
