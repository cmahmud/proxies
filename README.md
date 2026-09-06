# SyndProxy validated proxy pool

## Current pool

- Alive now: 483
- Gold now: 402
- HTTP: 92 alive / 65 gold
- HTTPS: 32 alive / 16 gold
- SOCKS4: 170 alive / 157 gold
- SOCKS5: 189 alive / 164 gold

## Historical pool

- Discovered: 218933
- Ever alive: 48250
- Ever gold: 1526

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
