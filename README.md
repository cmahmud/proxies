# SyndProxy validated proxy pool

## Current pool

- Alive now: 535
- Gold now: 414
- HTTP: 96 alive / 63 gold
- HTTPS: 87 alive / 21 gold
- SOCKS4: 165 alive / 160 gold
- SOCKS5: 187 alive / 170 gold

## Historical pool

- Discovered: 182503
- Ever alive: 35634
- Ever gold: 1260

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
