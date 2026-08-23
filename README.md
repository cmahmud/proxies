# SyndProxy validated proxy pool

## Current pool

- Alive now: 632
- Gold now: 201
- HTTP: 175 alive / 44 gold
- HTTPS: 164 alive / 9 gold
- SOCKS4: 115 alive / 65 gold
- SOCKS5: 178 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32679
- Ever gold: 1196

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
