# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 372
- HTTP: 190 alive / 88 gold
- HTTPS: 43 alive / 30 gold
- SOCKS4: 104 alive / 76 gold
- SOCKS5: 208 alive / 178 gold

## Historical pool

- Discovered: 223440
- Ever alive: 48615
- Ever gold: 1560

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
