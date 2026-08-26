# SyndProxy validated proxy pool

## Current pool

- Alive now: 501
- Gold now: 402
- HTTP: 93 alive / 61 gold
- HTTPS: 55 alive / 16 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 182 alive / 166 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38982
- Ever gold: 1295

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
