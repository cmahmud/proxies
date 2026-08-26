# SyndProxy validated proxy pool

## Current pool

- Alive now: 532
- Gold now: 399
- HTTP: 91 alive / 56 gold
- HTTPS: 81 alive / 15 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 188 alive / 167 gold

## Historical pool

- Discovered: 185576
- Ever alive: 39147
- Ever gold: 1297

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
