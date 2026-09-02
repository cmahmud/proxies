# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 443
- HTTP: 94 alive / 73 gold
- HTTPS: 119 alive / 31 gold
- SOCKS4: 172 alive / 162 gold
- SOCKS5: 188 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47450
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
