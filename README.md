# SyndProxy validated proxy pool

## Current pool

- Alive now: 545
- Gold now: 430
- HTTP: 119 alive / 80 gold
- HTTPS: 67 alive / 21 gold
- SOCKS4: 172 alive / 159 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 181494
- Ever alive: 33932
- Ever gold: 1253

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
