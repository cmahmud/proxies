# SyndProxy validated proxy pool

## Current pool

- Alive now: 507
- Gold now: 414
- HTTP: 81 alive / 60 gold
- HTTPS: 51 alive / 20 gold
- SOCKS4: 189 alive / 163 gold
- SOCKS5: 186 alive / 171 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47120
- Ever gold: 1465

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
