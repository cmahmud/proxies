# SyndProxy validated proxy pool

## Current pool

- Alive now: 562
- Gold now: 440
- HTTP: 92 alive / 69 gold
- HTTPS: 95 alive / 29 gold
- SOCKS4: 181 alive / 164 gold
- SOCKS5: 194 alive / 178 gold

## Historical pool

- Discovered: 208020
- Ever alive: 47467
- Ever gold: 1469

`alive/` is the current passing pool. `gold/` is the current repeatedly verified, higher-scoring subset. `historical/` is append-only and does not remove a proxy just because it later goes offline. `archive/` stores periodic snapshots of the current combined alive/gold pools.
