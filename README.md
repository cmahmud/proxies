# SyndProxy validated proxy pool

## Current pool

- Alive now: 566
- Gold now: 443
- HTTP: 98 alive / 75 gold
- HTTPS: 106 alive / 32 gold
- SOCKS4: 171 alive / 159 gold
- SOCKS5: 191 alive / 177 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47346
- Ever gold: 1466

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
