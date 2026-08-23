# SyndProxy validated proxy pool

## Current pool

- Alive now: 619
- Gold now: 149
- HTTP: 187 alive / 40 gold
- HTTPS: 83 alive / 4 gold
- SOCKS4: 152 alive / 22 gold
- SOCKS5: 197 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32679
- Ever gold: 1194

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
