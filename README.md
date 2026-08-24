# SyndProxy validated proxy pool

## Current pool

- Alive now: 514
- Gold now: 387
- HTTP: 109 alive / 56 gold
- HTTPS: 39 alive / 12 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 195 alive / 160 gold

## Historical pool

- Discovered: 178284
- Ever alive: 33364
- Ever gold: 1235

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
