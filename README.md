# SyndProxy validated proxy pool

## Current pool

- Alive now: 622
- Gold now: 195
- HTTP: 186 alive / 43 gold
- HTTPS: 98 alive / 4 gold
- SOCKS4: 144 alive / 65 gold
- SOCKS5: 194 alive / 83 gold

## Historical pool

- Discovered: 169346
- Ever alive: 32679
- Ever gold: 1195

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
