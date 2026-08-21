# SyndProxy private pool

## Current pool

- Alive now: 772
- Gold now: 393
- HTTP: 221 alive / 81 gold
- HTTPS: 115 alive / 17 gold
- SOCKS4: 206 alive / 148 gold
- SOCKS5: 230 alive / 147 gold

## Historical pool

- Discovered: 155789
- Ever alive: 29314
- Ever gold: 1125

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
