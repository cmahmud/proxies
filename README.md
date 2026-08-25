# SyndProxy validated proxy pool

## Current pool

- Alive now: 560
- Gold now: 428
- HTTP: 116 alive / 76 gold
- HTTPS: 91 alive / 24 gold
- SOCKS4: 167 alive / 157 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 182503
- Ever alive: 34908
- Ever gold: 1259

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
