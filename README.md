# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 442
- HTTP: 93 alive / 70 gold
- HTTPS: 114 alive / 32 gold
- SOCKS4: 172 alive / 163 gold
- SOCKS5: 190 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47406
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
