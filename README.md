# SyndProxy validated proxy pool

## Current pool

- Alive now: 573
- Gold now: 454
- HTTP: 92 alive / 78 gold
- HTTPS: 107 alive / 36 gold
- SOCKS4: 181 alive / 162 gold
- SOCKS5: 193 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47396
- Ever gold: 1468

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
