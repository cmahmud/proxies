# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 410
- HTTP: 118 alive / 65 gold
- HTTPS: 86 alive / 15 gold
- SOCKS4: 177 alive / 162 gold
- SOCKS5: 192 alive / 168 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38108
- Ever gold: 1289

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
