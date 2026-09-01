# SyndProxy validated proxy pool

## Current pool

- Alive now: 649
- Gold now: 468
- HTTP: 143 alive / 95 gold
- HTTPS: 122 alive / 37 gold
- SOCKS4: 183 alive / 164 gold
- SOCKS5: 201 alive / 172 gold

## Historical pool

- Discovered: 208020
- Ever alive: 46934
- Ever gold: 1457

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
