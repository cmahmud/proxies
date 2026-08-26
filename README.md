# SyndProxy validated proxy pool

## Current pool

- Alive now: 569
- Gold now: 407
- HTTP: 98 alive / 61 gold
- HTTPS: 92 alive / 14 gold
- SOCKS4: 172 alive / 161 gold
- SOCKS5: 207 alive / 171 gold

## Historical pool

- Discovered: 185576
- Ever alive: 38183
- Ever gold: 1290

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
