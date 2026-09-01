# SyndProxy validated proxy pool

## Current pool

- Alive now: 490
- Gold now: 412
- HTTP: 80 alive / 57 gold
- HTTPS: 53 alive / 21 gold
- SOCKS4: 175 alive / 163 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47118
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
