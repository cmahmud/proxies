# SyndProxy validated proxy pool

## Current pool

- Alive now: 515
- Gold now: 414
- HTTP: 84 alive / 60 gold
- HTTPS: 64 alive / 20 gold
- SOCKS4: 185 alive / 163 gold
- SOCKS5: 182 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47123
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
